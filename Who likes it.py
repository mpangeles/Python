#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
#[]                                -->  "no one likes this"
#["Peter"]                         -->  "Peter likes this"
#["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
#["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
#["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

#Mi solucion
def likes(names):

    x = len(names)
    first="no one likes"
    if x == 1:
     first=names[0]+" likes"
    elif x==2:
      first=names[0] +" and "+ names[1]+" like" 
    elif x==3:
     first=names[0] +", "+ names[1] +" and "+ names[2]+" like"
    elif x>3:
       first=names[0]+", "+names[1]+" and "+str(x-2)+" others like"

    text=f"{first} this"

    return text