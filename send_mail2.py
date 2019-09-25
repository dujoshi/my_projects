import os, sys, time, pdb

def send_mail( From, To, Sub, body ):
     SENDMAIL = "/usr/sbin/sendmail" # which send mail will  give this
     p = os.popen("%s -t" % SENDMAIL, "w")
     fr="From:" + From+"\n"
     to="To:" + To+"\n"
     p.write(fr)
     p.write(to)
     p.write("Subject:" + "Test Report "+ Sub +"\n")
     p.write("Content-Type: text/html;")
     p.write("\n") # blank line separating headers from body
     p.write(body) #body of the mail
     sts = p.close()
     if sts != 0:
          return 1
     return 0


def prepare_msg_body(take_report):
     #from take_report variable you can read and populate html msg
     # and then this msg can be sent in a mail

     time_taken='2Hour'
     Total_case=10
     Passed_case=9
     Failed_case=1
     Skiped_case=1
     MAIL_MSG=""" \n
                        <html><body> \n
                         <style type=\"text/css\">\n
                            .myTable { border-collapse:collapse; } \n
                            .myTable th { width:50%; } \n
                            .myTable td, .myTable th { padding:5px;border:1px solid #000; }\n
                            .myTable tr {style=\"border:1px solid black;\"} \n
                       </style> \n
                       <p> Total time taken by the suite is :<b> """+ time_taken + """</b>
                       <br>
                       <br>
                       <p><h2> Run Summary Report </h2> <p>
                       <table border="1" style="width:400px">
                       <tr><b> <font face ='Verdana' size ='2'><td> STATUS </td> <td> TOTAL </td> <td> PASS </td> <td> FAIL </td> <td> SKIP </td> </b></tr>
                       <tr> <font face ='Verdana' size ='2'><td> Completed </td>
                                         \t</td><td> """ + str(Total_case)+"""
                                         \t</td><td> """ + str(Passed_case)+"""
                                         \t</td><td> """ + str(Failed_case)+"""
                                         \t</td><td> """ + str(Skiped_case)+"""
                                         </td></font></p></tr> \n
                       </table>
                       <br>
                       <br>
                       <p> <h2> Failed TEST Detail :</h2> </p> \n
                       <table border="1" style="width:300px">
                       <tr><b> <font face ='Verdana' color='red' size ='2'> \
                               <td> S/No  </td>\
                               <td> Test Name </td>\
                               <td> Staus   </td>
                               <td> Time Taken </td>
                               <td> Owner </td>
                       </font></b></tr>
                       </body></html>
     """
     return MAIL_MSG


if not send_mail('dujoshi@cisco.com', 'dujoshi@cisco.com', 'hi',  prepare_msg_body('abc')):
      print 'ISSUE in sending mail '
