from telegram import ChatPermissions

participant_role = ChatPermissions(
    can_be_edited=False,
    can_change_info=False,
    can_post_messages=False,
    can_edit_messages=False,
    can_delete_messages=False,
    can_invite_users=False,
    can_restrict_members=False,
    can_pin_messages=False,
    can_promote_members=False,
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False
)
