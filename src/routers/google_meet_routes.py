from fastapi import APIRouter
from ..utils.meet_utils.join_meet import join_meeting
# END IMPORTS

google_meet_router = APIRouter()

# APIs


@google_meet_router.get('/record-meet')
async def record_meet():
    await join_meeting()
    return 'Recording..'
