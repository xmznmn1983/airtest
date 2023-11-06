import element_path as el
import action as action


tickets = action.poco("TicketPage").offspring("Content").offspring("Content").child()


def openBingoStore():
    action.click_button(el.ticket)


def checkTickets():
    for i in range(tickets.__len__()):
        for j in range(tickets[i].child().__len__()):
            el_name = tickets[i].child()[j]
            # print(el_name.get_name())
            if el_name.get_name() == "Amount":
                print(el_name.get_text())
                # print(el_name.focus([0.5, 0.5]).get_position())
                action.poco(text=el_name.get_text()).focus([0.5, 0.5]).click()


# def check_openBingoStore():
#     if child_element_exist(el.ticket) == True:
#         print()

# openBingoStore()
# checkTickets()

