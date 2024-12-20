async def check_subscribe(bot,message,channels_id):
    return True
    for channel in channels_id:
        if (await bot.get_chat_member(user_id=message.from_user.id, chat_id=channel)).status == 'left':
            return False
    return True
def add_to_db(user_id, database):
    if user_id not in database.list:
        database.list.append(user_id)

def save_db(num, database):
    if num != 10:
        num += 1
        return num
    database.dump()
    return num + 1

async def delete_old_message(user, messages):
    try:
        await messages[user].delete()
    except:
        return False

def dict_to_class(dict, clas):
    return clas(**dict)