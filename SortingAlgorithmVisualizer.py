import pygame
import random
import time

length = 1250
width = 850

arrlength = 400
arr=[]

sortspeed=0.01

def generateArray(n):
    tempArr= random.sample(range(1,n+1), n)
    return tempArr
    
    
def draw(arr, arrlength, pos, pyscreen):
    counter = pos
    for i in arr:
        counter+=1
        pyscreen.fill((255,255,255), ((counter - 1) *(length/arrlength), 0, (length/arrlength)-1, length))
        pygame.draw.rect(pyscreen, (37, 150, 190), ((counter - 1) *(length/arrlength), width-i*(width/arrlength), (length/arrlength)-1, i*(width/arrlength)))
    pygame.display.update()

def selectionSort(arr, pyscreen):
    for i in range(0, len(arr)):
        smallest=i
        for j in range(i, len(arr)):
            if arr[smallest] > arr[j]:
                smallest = j
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        draw(arr, arrlength, 0, pyscreen)
        time.sleep(sortspeed)

def insertionSort(arr, pyscreen):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j = j - 1
        draw(arr, arrlength, 0, pyscreen)
        time.sleep(sortspeed)

def bubbleSort(arr, pyscreen):
    for i in range(0, len(arr)):
        swap=False
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap=True
        if swap==False:
            break
        draw(arr, arrlength, 0, pyscreen)
        time.sleep(sortspeed)            
                
def mergeSort(arr, pos, pyscreen):
    if len(arr) > 1:

        mid = len(arr)//2

        left=arr[0:mid]
        right=arr[mid:len(arr)]

        mergeSort(left, pos, pyscreen)
        mergeSort(right, pos + len(arr)//2, pyscreen)

        i = 0
        j = 0
        k = 0

        print(left)
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            draw(arr, arrlength, pos, pyscreen)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            draw(arr, arrlength,  pos,  pyscreen)
            time.sleep(sortspeed)
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            draw(arr, arrlength, pos, pyscreen)
            time.sleep(sortspeed)



def quickSort(arr, low, high, pos, pyscreen):
    print("S")            
def main():

    pygame.init()
    pyscreen = pygame.display.set_mode((length,width))
    pyscreen.fill((255,255,255))
    pygame.display.update()
    arr = generateArray(arrlength)
    print(arr)
    runState = True
    draw(arr, arrlength, 0, pyscreen)
    quickSort([1,4,6,7,3,11,2], 0, 6, 0 ,pyscreen)

    while runState:

        pyscreen.fill((255,255,255))
        draw(arr, arrlength, 0, pyscreen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runState = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mergeSort(arr, 0, pyscreen)
                if event.key == pygame.K_DOWN:
                    insertionSort(arr, pyscreen)
                if event.key == pygame.K_LEFT:
                    selectionSort(arr, pyscreen)
                if event.key == pygame.K_UP:
                    bubbleSort(arr, pyscreen)    
                if event.key == pygame.K_r:
                    arr = generateArray(arrlength)
                    draw(arr, arrlength, 0, pyscreen)

    pygame.quit()
    
main()
    
