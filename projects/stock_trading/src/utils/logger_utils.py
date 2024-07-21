from . import os, sys
from loguru import logger

def setup_logger(level: str='DEBUG') -> None:
    """
    Set up the logger with the specified logging level and format.

    Parameters:
        level (str): Logging level ('DEBUG' or 'INFO').
    """    
    # Define logging level
    if level not in ['INFO', 'DEBUG']:
        raise ValueError("Level must be 'INFO' or 'DEBUG'.")
    
    # Remove any existing handlers
    logger.remove()

    # Add handler to log to standard output
    logger.add(sys.stdout, level=level, colorize=True, backtrace=True, diagnose=True)
    
    # Add handler to log to file in 1 day intervals
    log_dir = '../logs'
    os.makedirs(log_dir, exist_ok=True)
    logger.add(
        os.path.join(log_dir, '{time:YYYY-MM-DD}.log'),
        rotation="1 day",
        level=level,
        colorize=False,
        backtrace=True,
        diagnose=True,
        )

    logger.debug("Setting up logger...")
