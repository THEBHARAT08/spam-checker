data = None
try:
  with open('spamkey.txt','r') as f:
    data=(f.read())
    # data=data.split(', ')
    
    # print(data)
except FileNotFoundError:
  print("File not found!")



def find_spam(sentence,spam_list):
  sentence=sentence.lower()
  for word in spam_list:
    if word.lower() in sentence:
      print("Marked as spam!")
      return True
  print('The given sentence is safe.')   
  return False


x=find_spam("lets play rummy",data.split(', ') )
print(x)