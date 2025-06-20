import os
import requests
import icalendar
from typing import List

def get_calendar_events() -> List[dict]:
  url = os.getenv("CALENDAR_URL")
  
  response = requests.get(url)
  response.raise_for_status()
  
  cal = icalendar.Calendar.from_ical(response.content)
  
  #return response.content
  
  events = []
  for component in cal.walk():
    if component.name == "VEVENT":
      event = {
        "summary": str(component.get("summary")),
        "start": str(component.get("dtstart").dt),
        "end": str(component.get("dtend").dt),
        "location": str(component.get("location")),
      }
      events.append(event)
  return events
