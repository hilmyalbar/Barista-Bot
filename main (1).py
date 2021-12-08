print('hello!! welcome to albar coffe shop!!')
name = input('what is your name? ')
order = input('okay '+name+', we are serving some tea, cappucino, espresso, and coffe\nwhat do you want order for today? ')
if order == "tea":
  quantity = input('how much '+order+' do you want? (number) ')
  total = int(quantity)*2000
  print(30*'=')
  print('the total will be '+ str(total) + " idr")
  print(30*'=')
elif order == "cappucino":
  quantity = input('how much '+order+' do you want? (number) ')
  total = int(quantity)*7000
  print(30*'=')
  print('the total will be '+ str(total) + ' idr')
  print(30*'=')
elif order == "espresso":
  quantity = input('how much '+order+' do you want? (number) ')
  total = int(quantity)*8000
  print(30*'=')
  print('the total will be '+ str(total) + ' idr')
  print(30*'=')
elif order == "coffe":
  quantity = input('how much '+order+' do you want? (number) ')
  total = int(quantity)*5000
  print(30*'=')
  print('the total will be '+ str(total) + ' idr')
  print(30*'=')
else:
  total = 0
  print('sorry we aren\'t serving that')
tambahan = input('is there anything else? (y / n) ')
if tambahan == 'y':
  order = input('what do you want order for now? (tea, cappucino, espresso, coffe) ')
  if order == "tea":
    quantity = input('how much ' + order + ' do you want? (number) ')
    total = total + int(quantity)*2000
    print(30*'=')
    print('there will be ' + str(total) + ' idr')
    print(30*'=')
    print('okay '+name+', we will have your order in a few moment')
  elif order == "cappucino":
    quantity = input('how much ' + order + ' do you want? (number) ')
    total = total + int(quantity)*7000
    print(30*'=')
    print('there will be ' + str(total) + ' idr')
    print(30*'=')
    print('okay '+name+', we will have your order in a few moment')
  elif order == "espresso":
    quantity = input('how much ' + order + ' do you want? (number) ')
    total = total + int(quantity)*7000
    print(30*'=')
    print('there will be ' + str(total) + ' idr')
    print(30*'=')
    print('okay '+name+', we will have your order in a few moment')
  elif order == "coffe":
    quantity = input('how much ' + order + ' do you want? (number) ')
    total = total + int(quantity)*5000
    print(30*'=')
    print('there will be ' + str(total) + ' idr')
    print(30*'=')
    print('okay '+name+', we will have your order in a few moment')
  else:
    print('sorry we are not serving that!!')
    
if tambahan == "n":
  print('okay '+name+', we will have your order in a few moment')
 

  
