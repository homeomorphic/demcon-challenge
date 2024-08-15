
from collections import namedtuple
import sys
from matplotlib import pyplot as plt

Task = namedtuple("Task", ["name", "start", "end"])
Event = namedtuple("Event", ["time", "event_type", "task_num"])


def main():
    tasks = read_tasks_from_stdin()
    assignment = assign_tasks_to_slots(tasks)
    plot(tasks, assignment)


def read_tasks_from_stdin():
    tasks = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        name, start_str, end_str = line.split()
        start, end = int(start_str), int(end_str)
        task = Task(name=name, start=start, end=end)
        tasks.append(task)
    return tasks        


def assign_tasks_to_slots(tasks):
    events = []
    for task_num, task in enumerate(tasks):
        start_event = Event(task.start, 0, task_num)
        end_event = Event(task.end, 1, task_num)
        events.append(start_event)
        events.append(end_event)
    events.sort()

    assignment = {}
    slots = []
    available_slots = [] 
    for time, event_type, task_num in events:
        if event_type == 0:
            # Start event
            if available_slots:
                slot = available_slots.pop(0)
                assignment[task_num] = slot
            else:
                slot = len(slots)
                slots.append(slot)
                assignment[task_num] = slot
        else:
            # End event
            available_slots.append(assignment[task_num])

    return assignment


def plot(tasks, assignment):
    max_slot = 0
    for task_num, task in enumerate(tasks):
        slot = assignment[task_num]
        max_slot = max(slot, max_slot)
        duration = task.end - task.start + 1
        plt.barh(y=slot+1, left=task.start, width=duration)
        plt.text(task.start, slot+1, task.name, fontsize='x-small')
        print(f"Show {task.name} is scheduled on stage {slot+1}")
    plt.title(f'Schedule with {max_slot+1} stages')
    plt.xlabel('Time [h]')
    plt.ylabel('Stage number [1]')
    plt.grid(axis='x')
    plt.show()


if __name__ == "__main__":
    main()

