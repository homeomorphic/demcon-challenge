
import sys
from collections import namedtuple

from matplotlib import pyplot as plt


Task = namedtuple("Task", ["task_num", "name", "start", "end"])
Event = namedtuple("Event", ["time", "event_type", "task"])

START = 0
END = 1


def main():
    tasks = read_tasks_from_stdin()
    assignment = assign_tasks_to_slots(tasks)
    plot(assignment)


def read_tasks_from_stdin():
    """Read the tasks from the standard input and returns them as a list.
    The input tasks are expected to be of the form:
        show_1 36 39
        show_2 30 33
        show_3 29 36"""
    tasks = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        name, start_str, end_str = line.split()
        start, end = int(start_str), int(end_str)
        task_num = len(tasks)
        task = Task(task_num=task_num, name=name, start=start, end=end)
        tasks.append(task)
    return tasks        


def assign_tasks_to_slots(tasks):
    """Assigns the given tasks to slots so that no two tasks that overlap are on the
    same slot. This routine minimizes the number of slots used.
    The result will be a dictionary mapping tasks to a (0-based) slot number."""
    events = []
    for task in tasks:
        # Since a task ending at time T and starting at time T overlap,
        # we must process start events prior to end events.
        assert START < END 
        start_event = Event(task.start, START, task)
        end_event = Event(task.end, END, task)
        events.append(start_event)
        events.append(end_event)
    events.sort()

    assignment = {}
    slots = []
    available_slots = [] 
    for time, event_type, task in events:
        if event_type == START:
            if available_slots:
                slot = available_slots.pop(0)
                assignment[task] = slot
            else:
                slot = len(slots)
                slots.append(slot)
                assignment[task] = slot
        else:
            available_slots.append(assignment[task])

    return assignment


def plot(assignment):
    """Plot the given assignment of tasks to slots."""
    max_slot = 0
    for task, slot in assignment.items():
        max_slot = max(slot, max_slot)
        duration = task.end - task.start + 1
        plt.barh(y=slot+1, left=task.start, width=duration)
        plt.text(task.start, slot+1, task.name, fontsize="x-small")
        print(f"Show {task.name} is scheduled on stage {slot+1}")
    plt.title(f"Schedule with {max_slot+1} stages")
    plt.xlabel("Time [h]")
    plt.ylabel("Stage number [1]")
    plt.grid(axis="x")
    plt.show()


if __name__ == "__main__":
    main()

