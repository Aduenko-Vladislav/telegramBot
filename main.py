import telebot
from telebot import types
import os

waiting_for_contact = False
class Product:
    def __init__(self, name, description, image_filename):
        self.name = name
        self.description = description
        self.image_filename = image_filename

class ProductList:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Cart:
    def __init__(self):
        self.items = {}

class UserCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product_index, quantity):
        if product_index in self.items:
            self.items[product_index] = max(0, quantity)
        else:
            self.items[product_index] = max(0, quantity)

    def remove_item(self, product_index):
        if product_index in self.items:
            del self.items[product_index]

    def calculate_total(self):
        total = 0
        for product_index, quantity in self.items.items():
            total += quantity * calculate_item_price(quantity)
        return total

def calculate_item_price(quantity):
    if quantity > 9:
        return 70
    else:
        return 80

user_carts = {}

cart = Cart()

product_list = ProductList()


# Добавляем товары
product_list.add_product(Product('Sakura grape (Сакура и виноград)', 'Яркая вишнёвая сладость с оттенками винограда.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/sakura-grape.jpg'))
product_list.add_product(Product('Watermelon ice (Арбузный лед)', 'Освежающий арбуз, приправленный прохладным ментоловым холодком.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/watermelon-ice.jpg'))
product_list.add_product(Product('Red mojito (Красный мохито)', 'Экзотический мохито с красными фруктами и легкой кислинкой.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/red-mogito.jpg'))
product_list.add_product(Product('Blue razz ice (Сине-малиновый лед)', 'Сочная малина, обволакиваемая мороженой свежестью.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/blue-razz-ice.jpg'))
product_list.add_product(Product('Lemon mint (Лимон с мятой)', 'Яркий лимон, приправленный ароматной мятой.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/lemon-mint.jpg'))
product_list.add_product(Product('Mango peach (Манго с персиком)', 'Сладкий манго и спелый персик в одном вдохе.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/mango-peach.jpg'))
product_list.add_product(Product('Cranberry grape (Клюквенно-виноградный)', 'Смесь клюквы и винограда с легкой кислинкой.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/cranberry-grape.jpg'))
product_list.add_product(Product('Tropical rainbow blast (Тропический радужный взрыв)', 'Взрыв тропических фруктовых вкусов в каждой затяжке.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/tropical_blast.jpg'))
product_list.add_product(Product('Watermelon bubblegum (Арбузная жвачка)', 'Вкус сладкой жвачки, сочетающейся с арбузной сладостью.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/watermelon-bubblegum.jpg'))
product_list.add_product(Product('Peach ice (Персиковый лед)', 'Сочный персик с освежающим ледяным холодком.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/peach-ice.jpg'))
product_list.add_product(Product('Strawberry banana (Клубника с бананом)', 'Сладкая клубника и кремовый банан в одной электронной сигарете.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/strawberry-banana.jpg'))
product_list.add_product(Product('Triple berry ice (Тройной ягодный лед)', 'Смесь трёх ягод, завёрнутая в холодное мороженое.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/triple-berry-ice.jpg'))
product_list.add_product(Product('Blueberry ice (Черничный лед)', 'Сочная черника с ментоловым ледяным акцентом.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/Blueberry-ice.jpg'))
product_list.add_product(Product('Summer peach ice (Летний персиковый лед)', 'Летний бриз с ароматом спелого персика и легкой ментоловой прохладой.\n\nЦена 80₪/шт \nПри покупке от 10 позиций - 70₪/шт', 'images/Summer-peach-ice.jpg'))


bot = telebot.TeleBot('token')


@bot.message_handler(commands=['contact'])
def request_contact(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    contact_button = types.KeyboardButton("Отправить контакт", request_contact=True)
    markup.add(contact_button)
    bot.send_message(message.chat.id, "Пожалуйста, отправьте свой контактный номер телефона.", reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['contact'])
def process_contact(message):
    contact = message.contact
    phone_number = contact.phone_number if contact and contact.phone_number else None
    avatarname = message.from_user.username if message.from_user.username else "нет никнейма"
    username = f"{contact.first_name} {contact.last_name}" if contact and (contact.first_name or contact.last_name) else "нет username"
    telegram_username = contact.username if contact and hasattr(contact, 'username') and contact.username else "нет Telegram username"

    bot.send_message(message.chat.id, f"Спасибо! Ваш номер телефона ({phone_number}) отправлен менеджеру.\n"
                     f'Менеджер свяжется с Вами в ближайшее время!🤘🏾\n')

    # Отправьте информацию о контакте менеджеру
    bot.send_message("manager_id", f'🤘🏾Клиент просит связаться с ним для заказа:\n'
                                f'Номер телефона: {phone_number}\n'
                                f'Username: {username}\n'
                                f'Ник: @{avatarname}\n')





@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.chat.id
    user_carts[user_id] = UserCart()
    send_welcome(user_id)

def send_welcome(chat_id):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('📱Перейти на инстаграмм', url='https://instagram.com/elfbr_israel?igshid=OGQ5ZDc2ODk2ZA==')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('🛒Каталог товаров', callback_data='main_menu')
    markup.row(btn2)

    file = open('./elfbar.jpg', 'rb')
    bot.send_photo(chat_id, file, reply_markup=markup, caption='🛒Добро пожаловать в чат-бот Telegram, по заказу ELFBAR в Израиле\n\n'
   '✅ Здесь можно ознакомиться с каталогом товаров, заказать доставку, связаться с менеджером!')

@bot.callback_query_handler(func=lambda call: call.data == 'main_menu')
def main_menu(callback):
    send_product_menu(callback.message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == 'back_to_menu')
def back_to_menu(callback):
    send_welcome(callback.message.chat.id)

def send_product_menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    for i, product in enumerate(product_list.products):
        btn = types.InlineKeyboardButton(product.name, callback_data=f'product_{i}')
        markup.add(btn)
    file = open('./elfbar_flavours.jpg', 'rb')
    btn15 = types.InlineKeyboardButton('↩️ Назад в меню', callback_data='back_to_menu')
    markup.add(btn15)
    bot.send_photo(chat_id, file, reply_markup=markup, caption='1️⃣Цена за 1 - 80₪₪\n🔟При покупке от 10 позиций - 70₪/шт\n\nДоставка от 5шт - бесплатная\n\n🛒Выберите товар из списка:')



@bot.callback_query_handler(func=lambda call: call.data.startswith('product_'))
def product_description(callback):
    product_index = int(callback.data.split('_')[1])
    send_product_description(callback.message.chat.id, product_index, quantity=1)

def send_product_description(chat_id, product_index, quantity):
    product = product_list.products[product_index]
    description = f"{product.name}\n\n{product.description}"
    markup = create_product_description_markup(product_index, quantity)

    image_path = os.path.join(os.getcwd(), product.image_filename)
    bot.send_photo(chat_id, open(image_path, 'rb'), reply_markup=markup, caption=description)

def create_product_description_markup(product_index, quantity):
    markup = types.InlineKeyboardMarkup()

    # Ряд с кнопкой "Добавить в корзину"
    add_to_cart_button = types.InlineKeyboardButton('🛒Добавить в корзину',
                                                    callback_data=f'add_to_cart_{product_index}')
    markup.row(add_to_cart_button)
    # Ряд с кнопкой "назад в каталог"
    back_to_catalog_button = types.InlineKeyboardButton('↩️ Назад в каталог', callback_data='back_to_catalog')
    markup.row(back_to_catalog_button)

    return markup

@bot.callback_query_handler(func=lambda call: call.data.startswith('add_to_cart_'))
def add_to_cart(callback):
    product_index = int(callback.data.split('_')[-1])
    user_id = callback.message.chat.id
    if user_id not in user_carts:
        user_carts[user_id] = UserCart()
    user_carts[user_id].add_item(product_index, 1)

    send_quantity_selection(callback.message, product_index, callback.message.chat.id, quantity=1)
    bot.delete_message(callback.message.chat.id, callback.message.message_id)




def send_quantity_selection(message, product_index, chat_id, quantity):
    product = product_list.products[product_index]
    description = f"{product.name}\n\n{product.description}"
    markup = create_quantity_selection_markup(product_index, quantity)

    image_path = os.path.join(os.getcwd(), product.image_filename)

    bot.send_photo(chat_id, open(image_path, 'rb'), caption=description, reply_markup=markup)


def create_quantity_selection_markup(product_index, quantity):
    markup = types.InlineKeyboardMarkup()

    if quantity > 0:
        # Ряд с кнопками "+", "-", и "количество позиций"
        quantity_buttons = [
            types.InlineKeyboardButton('➖', callback_data=f'change_quantity_{product_index}_{quantity - 1}'),
            types.InlineKeyboardButton(f'{quantity}', callback_data=f'change_quantity_{product_index}_{quantity}'),
            types.InlineKeyboardButton('➕', callback_data=f'change_quantity_{product_index}_{quantity + 1}'),
        ]
        markup.row(*quantity_buttons)

    else:
        # Если количество товара равно 0, добавляем кнопку "Добавить в корзину"
        add_to_cart_button = types.InlineKeyboardButton('🛒Добавить в корзину',
                                                        callback_data=f'add_to_cart_{product_index}')
        markup.row(add_to_cart_button)

    # Если количество товара больше 0, добавляем кнопку "Удалить"
    if quantity > 0:
        delete_button = types.InlineKeyboardButton('❌Удалить', callback_data=f'delete_product_{product_index}')
        markup.row(delete_button)

    # Ряд с кнопкой "перейти в корзину"
    go_to_cart_button = types.InlineKeyboardButton('🛍Перейти в корзину', callback_data='go_to_cart')
    markup.row(go_to_cart_button)

    # Ряд с кнопкой "назад в каталог"
    back_to_catalog_button = types.InlineKeyboardButton('↩️ Назад в каталог', callback_data='back_to_catalog')
    markup.row(back_to_catalog_button)

    return markup


@bot.callback_query_handler(func=lambda call: call.data.startswith('delete_product_'))
def delete_product(callback):
    product_index = int(callback.data.split('_')[-1])
    user_carts[callback.message.chat.id].remove_item(product_index)

    # Обновим карточку товара
    send_quantity_selection(callback.message, product_index, callback.message.chat.id, quantity=0)





@bot.callback_query_handler(
    func=lambda call: call.data.startswith('change_quantity_'))
def handle_quantity_callback(call):
    try:
        # Извлекаем данные из callback data
        data_parts = call.data.split('_')
        product_index = int(data_parts[2])
        new_quantity = int(data_parts[3])

        # Обновляем количество в корзине
        user_carts[call.message.chat.id].add_item(product_index, new_quantity)

        # Отправляем обновленную разметку блока кнопок
        markup = create_quantity_selection_markup(product_index, new_quantity)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)

    except IndexError:
        print("IndexError: list index out of range")

    except Exception as e:
        print(e)




def create_cart_quantity_markup(product_index, quantity):
    markup = types.InlineKeyboardMarkup()

    # Ряд с кнопками "+", "-", и "количество позиций"
    quantity_buttons = [
        types.InlineKeyboardButton('➖', callback_data=f'change_quantity_{product_index}_{quantity - 1}'),
        types.InlineKeyboardButton(f'{quantity}', callback_data=f'change_quantity_{product_index}_{quantity}'),
        types.InlineKeyboardButton('➕', callback_data=f'change_quantity_{product_index}_{quantity + 1}'),
    ]
    markup.row(*quantity_buttons)

    return markup

@bot.callback_query_handler(func=lambda call: call.data == 'go_to_cart')
def go_to_cart(callback):
    send_cart_contents(callback.message.chat.id)

@bot.callback_query_handler(func=lambda call: call.data == 'contact_manager')
def contact_manager(callback):
    global waiting_for_contact
    waiting_for_contact = True
    send_cart_contents(callback.message.chat.id)


def send_cart_contents(chat_id):
    global waiting_for_contact

    if waiting_for_contact:
        # Отправляем кнопку "Отправить контакт"
        contact_button = types.KeyboardButton('Отправить контакт', request_contact=True)
        contact_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contact_markup.add(contact_button)
        bot.send_message(chat_id, 'Пожалуйста, отправьте ваш номер телефона, нажав на кнопку "Отправить контакт".',
                        reply_markup=contact_markup)

        # Передаем детали заказа в обработчик контакта
        bot.register_next_step_handler_by_chat_id(chat_id,
                                                  lambda message: handle_contact(message, None))

        waiting_for_contact = False  # Сбрасываем состояние
        return

    if not user_carts[chat_id].items:
        bot.send_message(chat_id, 'Ваша корзина пуста.')
        return

    total_quantity = sum(user_carts[chat_id].items.values())  # Общее количество товаров в корзине
    total_price = calculate_total_price(total_quantity)  # Общая стоимость заказа

    message_text = f"Ваш заказ:\n\n"

    for product_index, quantity in user_carts[chat_id].items.items():
        product = product_list.products[product_index]
        item_total = quantity * calculate_item_price(quantity)  # Рассчитываем стоимость товара
        message_text += f"{product.name} - {quantity} шт. - {item_total}₪\n"


    if total_quantity > 0:  # Добавили условие проверки наличия товаров в корзине
        message_text += f"\nИтого: {total_price}₪"

        # Добавляем кнопку "Связаться с менеджером"
        markup = types.InlineKeyboardMarkup()
        contact_manager_button = types.InlineKeyboardButton('🙋🏻‍♂️Перейти к оформлению заказа',
                                                            callback_data='contact_manager')
        markup.row(contact_manager_button)
    else:
        bot.send_message(chat_id, 'Ваша корзина пуста.')
        return

    # Кнопка "Назад в каталог" всегда будет присутствовать
    back_to_catalog_button = types.InlineKeyboardButton('↩️ Назад в каталог', callback_data='back_to_catalog')
    markup.row(back_to_catalog_button)

    # Отправляем сообщение с итогами заказа и кнопкой "Связаться с менеджером" или без нее
    bot.send_message(chat_id, message_text, reply_markup=markup)


def calculate_total_price(total_quantity):
    # Рассчитываем общую стоимость заказа
    if total_quantity > 9:
        return total_quantity * 70
    else:
        return total_quantity * 80


@bot.message_handler(func=lambda message: True, content_types=['contact'])
def handle_contact(message, details):
    global waiting_for_contact

    details = []
    chat_id = message.chat.id

    for product_index, quantity in user_carts[chat_id].items.items():
        product = product_list.products[product_index]
        item_total = quantity * calculate_item_price(quantity)

        details.append(f"{product.name} - {quantity} шт. - {item_total}₪")


    contact = message.contact
    if contact:
        phone_number = contact.phone_number if contact and contact.phone_number else None
        username = f"{contact.first_name} {contact.last_name}" if contact and (contact.first_name or contact.last_name) else "нет username"
        telegram_username = contact.username if contact and hasattr(contact, 'username') and contact.username else "нет Telegram username"
        avatarname = message.from_user.username if message.from_user.username else "нет никнейма"


        total_quantity = sum(user_carts[message.chat.id].items.values())
        total_price = calculate_total_price(total_quantity)

        user_carts.pop(chat_id)

        if total_quantity > 9:
            bot.send_message(message.chat.id,
                             f'🖤Спасибо! Ваш заказ успешно отправлен. Менеджер свяжется с вами в ближайшее время.\n'
                             f'Общее количество товаров: {total_quantity}\n'
                             f'Общая цена: {total_price}₪\n')
        else:
            bot.send_message(message.chat.id,
                             f'🖤Спасибо! Ваш заказ успешно отправлен. Менеджер свяжется с вами в ближайшее время.\n'
                             f'Общее количество товаров: {total_quantity}\n'
                             f'Общая цена: {total_price}₪\n'
                             f'При заказе от 10 шт: 70₪/штука')

        # Отправьте информацию о контакте, заказе, username, общем количестве и цене менеджеру
        bot.send_message(manager_id, f'🤘🏾Новый заказ от клиента:\n'
                                    f'Номер телефона: {phone_number}\n'
                                    f'Username: {username}\n'
                                    f'Ник: @{avatarname}\n'
                                    f'Заказ:\n{"\n".join(details)}\n'
                                    f'Общее количество товаров: {total_quantity}\n'
                                    f'Общая цена: {total_price}₪\n')

        waiting_for_contact = False
    else:
        bot.send_message(message.chat.id, 'Не удалось получить информацию о контакте. Пожалуйста, повторите попытку.')



@bot.callback_query_handler(func=lambda call: call.data == 'back_to_catalog')
def back_to_catalog(callback):
    send_product_menu(callback.message.chat.id)

def reset_cart():
    global cart
    cart = Cart()

if __name__ == "__main__":
    while True:
        try:
            print("Start bot")
            bot.polling(none_stop=True)
        except KeyboardInterrupt:
            exit(0)
        except Exception as ex:
            print("Error: ", ex)
            pass
