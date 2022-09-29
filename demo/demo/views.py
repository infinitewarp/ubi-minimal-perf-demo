from logging import getLogger
from django.http import HttpResponse

logger = getLogger(__name__)

def index(request):
    logger.info("hello")
    for _ in range(10):
        logger.info("dummy log message %s", _)
    return HttpResponse("Hello!")
