# Interview Scheduler
This project can be used to register time slots of different users and find the matching time slots.
Application can be run using command: docker compose up

There are 2 API end points

1. http://127.0.0.1:8000/register/
    POST Data Format
      {
        "user_id": 1,
        "from_time": "24-05-2020 20:00",
        "to_time": "24-05-2020 22:00",
      }
      
2. http://127.0.0.1:8000/slots/?interviewer_id=1&candidate_id=2&duration=.5
    GET params
      interviewer_id (Mandatory)
      candidate_id (Mandatory)
      duration (Optional, Required duration in hours, default 1 hour.)
    
