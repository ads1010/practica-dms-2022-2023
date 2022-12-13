""" DiscussionLogic class module.
"""

import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results import Report
from dms2223backend.data.db.resultsets import Reports
from dms2223backend.data.db.exc import DiscussionExistsError


class ReportLogic():
    """ Class with logic-level operations with the discussion-related use cases.
    """
    @staticmethod
    def create(session: Session, title: str, content: str) -> Report:
        """ Creates a new report record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - title (str): The title of the report string.
            - content (str): The content of the report string.

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - reportExistsError: If a user with the same username already exists.

        Returns:
            - report: The created `report` result.
        """
        
        try:
            new_report: Report = Reports.create(session, title, content)
           
        except Exception as ex:
            raise ex
        return new_report

    @staticmethod
    def list_all(session: Session) -> List[List]:
        """Lists every report.

        Args:
            - session (Session): The session object.

        Returns:
            - List[Report]: A list of `Report` registers.
        """

        return Reports.list_all(session)

    @staticmethod
    def get_report_by_id(session: Session, id: int,) -> Optional[Report]:
        """Obtains a rerport by an id.
        Args:
            - session (Session): The session object.
            - id (int): Id report integer.

        Returns:
            - Optional[Report]: The result of the `Report`.
        """

        try:
            report = Reports.get_report_by_id(session, id)
        except Exception as ex:
            raise ex
        return report

    