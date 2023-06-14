from apscheduler.events import (
    EVENT_JOB_ERROR,
    EVENT_JOB_EXECUTED,
)

from extensions import scheduler

def job_error(event):
    """Job error event."""
    with scheduler.app.app_context():
        print(event)  


def job_executed(event):
    """Job executed event."""
    with scheduler.app.app_context():
        print(event)

scheduler.add_listener(job_error, EVENT_JOB_ERROR)
scheduler.add_listener(job_executed, EVENT_JOB_EXECUTED)

