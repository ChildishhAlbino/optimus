from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent
import logging

class OptimusFileSystemHandler(FileSystemEventHandler):
    def __init__(self, *, logger: logging.Logger | None = None) -> None:
        super().__init__()
        self.logger = logger or logging.root

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        super().on_created(event)

        what = "directory" if event.is_directory else "file"
        self.logger.info("Created %s: %s", what, event.src_path)