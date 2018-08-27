import csv

class State:
  def __init__(self, asset, usage):
    self.asset = asset
    self.usage = usage

class Player:
  def __init__(self, name):
    self.name = name
    self.state = []
    self.state.append(State('wood', 'house'))
    self.state.append(State('wood', None))
    self.state.append(State('worker', 'wood'))
    self.state.append(State('worker', None))

# requirements would be more sophisticated like 'more trees than people'
# but keeping it simple for now
class Requirement:
  def __init__(self, requirement):
    self.requirement = requirement

class Result:
  def __init__(self, result):
    self.result = result

class Event:
  def __init__(self, requirement, phrase, result):
    self.requirement = requirement
    self.phrase = phrase
    self.result = result

events = []

with open('events.csv', 'rb') as csvFile:
    eventReader = csv.reader(csvFile, delimiter='|', quotechar='"')
    for event in eventReader:
        events.append(Event(Requirement(event[0]), event[1], Result(event[2])))

name = raw_input('Name you self: ')
player = Player(name)
resources = ['wood', 'worker']

quit = False

while quit == False:
  for resource in resources:
    totalQuantity = 0
    freeQuantity = 0

    for state in player.state:
      if state.asset == resource:
        totalQuantity += 1
        if state.usage == None:
          freeQuantity += 1
    
    print 'you have %i %s and %i spare' % (totalQuantity, resource, freeQuantity)

  for i, event in enumerate(events):
    #I'm going to be hella lazy here

    yeahPrintItIGuess = False

    for state in player.state:
      if state.asset == event.requirement.requirement and state.usage == None:
        yeahPrintItIGuess = True

    if yeahPrintItIGuess:
      print '[' + str(i) + '] ' + event.phrase % player.name

  input = raw_input('What want do (quit to quit): ')

  try:
    value = int(input)
    if value >= 0 and value < len(events):
      event = events[value]
      
      updated = False
      for i, state in enumerate(player.state):
        if state.asset == event.requirement.requirement and state.usage == None and updated == False:
          updated = True
          player.state[i].usage = event.result.result

      if updated:
        player.state.append(State(event.result.result, None))

  except ValueError:
    pass

  quit = input == 'quit'
