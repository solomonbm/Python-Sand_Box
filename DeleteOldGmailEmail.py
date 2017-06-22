import getpass, imaplib, datetime



def connect_imap():
    user = input("Enter your GMail username:")
    pwd = getpass.getpass("Enter your password: ")
    # connecting to the gmail imap server
    m = imaplib.IMAP4_SSL("imap.gmail.com")
    print("{0} Connecting to mailbox via IMAP...".format(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
    m.login(user+'@gmail.com', pwd)
 
    return m
 
 
 
def move_to_trash_before_date(m):
    print("Select which folder to Delete from: ")
    print(m.list()) # get all the mailboxes
    folder = raw_input("\n")
    no_of_msgs = int(m.select(folder)[1][0])  # required to perform search, m.list() for all lables, '[Gmail]/Sent Mail'
    print("- Found a total of {1} messages in '{0}'.".format(folder, no_of_msgs))
 
    days_back = int(input("Enter how many days back you wnat to keep: "))
    before_date = (datetime.date.today() - datetime.timedelta(days_back)).strftime("%d-%b-%Y")  # date string, 04-Jan-2013    
    rv, data = m.search(None, '(BEFORE {0})'.format(before_date))  # search pointer for msgs before before_date

    if rv != 'OK':
        print("No messages found!")
        return
    
    if data != ['']:  # if not empty list means messages exist
        no_msgs_del = len(data[0].split())
        print("- Marked {0} messages for removal with dates before {1} in '{2}'.".format(no_msgs_del, before_date, folder))
        m.store("1:{0}".format(no_msgs_del), '+X-GM-LABELS', '\\Trash')  # move to trash
        print("Deleted {0} messages.".format(no_msgs_del))
    else:
        print("- Nothing to remove.")
 
    return
 
 
def empty_folder(m, folder, do_expunge=True):
    print("- Empty '{0}' & Expunge all mail...".format(folder))
    m.select(folder)  # select all trash
    m.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
    if do_expunge:  # See Gmail Settings -> Forwarding and POP/IMAP -> Auto-Expunge
        m.expunge()  # not need if auto-expunge enabled
    else:
        print("Expunge was skipped.")
    return
 
 
def disconnect_imap(m):
    print("{0} Done. Closing connection & logging out.".format(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
    m.close()
    m.logout()
    #print "All Done."
    return
 

def main():

    m_con = connect_imap()
 
    move_to_trash_before_date(m_con)
                              
    empty_folder(m_con, '[Gmail]/Trash', do_expunge=True)  # can send do_expunge=False, default True
 
    disconnect_imap(m_con)

                              
if __name__ == '__main__':
    main()     
