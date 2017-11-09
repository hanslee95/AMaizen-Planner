import json
import time
import requests

class ScheduleApiError(Exception):
    '''
    Raised if there is an error with the schedule API.
    '''
    pass

# The base API endpoint
base_url = 'http://umich-schedule-api.herokuapp.com'

# the amount of time to wait for the schedule API
timeout_duration = 25


def get_data(relative_path):
    '''
    Gets data from the schedule API at the specified path.
    Will raise a ScheduleApiError if unsuccessful.
    Assumes API will return JSON, returns as a dictionary.
    '''

    timeout_at = time.time() + timeout_duration

    while time.time() < timeout_at:
        r = requests.get(base_url + relative_path)
        if r.status_code == 200:
            return json.loads(r.text)
        if r.status_code == 400:
            break

    raise ScheduleApiError('error for url: {0} message: "{1}" code: {2}' \
        .format(relative_path, r.text, r.status_code))

def get_terms():

    '''
    Returns a list of valid terms.
    Each item in the list is a dictionary containing:
        ('TermCode', 'TermDescr', 'TermShortDescr')
    '''
    return get_data('/get_terms')

def get_schools(TermCode):

    return get_data('/get_schools?term_code='+str(TermCode))

def get_subjects(TermCode, SchoolCode):
    
    return get_data('/get_subjects?term_code='+str(TermCode)+'&school='+SchoolCode)

def get_catalog_numbers(TermCode, SchoolCode, SubjectCode):

    return get_data('/get_catalog_numbers?term_code='+str(TermCode)+'&school='+SchoolCode+'&subject='+SubjectCode)

def get_course_description(TermCode, SchoolCode, SubjectCode, CatalogNumber):

    return get_data('/get_course_description?term_code='+str(TermCode)+'&school='+SchoolCode+'&subject='+SubjectCode+'&catalog_num='+str(CatalogNumber))

def get_section_nums(TermCode, SchoolCode, SubjectCode, CatalogNumber):

    return get_data('/get_section_nums?term_code='+str(TermCode)+'&school='+SchoolCode+'&subject='+SubjectCode+'&catalog_num='+str(CatalogNumber))

def get_section_details(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):

    return get_data('/get_section_details?term_code='+str(TermCode)+'&school='+SchoolCode+'&subject='+SubjectCode+'&catalog_num='+str(CatalogNumber)+'&section_num='+str(SectionNumber))

def get_meetings(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):

    return get_data('/get_meetings?term_code='+str(TermCode)+'&school='+SchoolCode+'&subject='+SubjectCode+'&catalog_num='+str(CatalogNumber)+'&section_num='+str(SectionNumber))

def get_textbooks(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):

    return get_data('/get_textbooks?term_code='+str(TermCode)+'&school='+SchoolCode+'&subject='+SubjectCode+'&catalog_num='+str(CatalogNumber)+'&section_num='+str(SectionNumber))

def get_instructors(TermCode, SchoolCode, SubjectCode, CatalogNumber, SectionNumber):

    return get_data('/get_instructors?term_code='+str(TermCode)+'&school='+SchoolCode+'&subject='+SubjectCode+'&catalog_num='+str(CatalogNumber)+'&section_num='+str(SectionNumber))