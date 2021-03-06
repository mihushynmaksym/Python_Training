
import re
__author__ = "Max"


def test_phones_on_home_page(app):  # reverse check
    app.group.find_home_button()
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert clear(contact_from_home_page.all_phones_from_home_page) == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):  # run without "clear" pattern
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[()+!? -]", "", s)  # filter clear pattern for forms.


def merge_phones_like_on_home_page(contact):  # merge all phones filter and assert
        return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),filter(lambda x: x is not None,
                                                     [contact.homephone, contact.mobilephone, contact.workphone,
                                                      contact.secondaryphone]))))

