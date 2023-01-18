# Importing the necessary packages
import sys
import os
import datetime
import emoji 
from csv import writer

# Defing the class for binary search tree
class BinarySearchTreeNode:

#1. Inserting the node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

#2. Searching the node
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

#3. Inorder Traversal
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

#3. Deleting the node
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

# Sorting the value using insertion Sort
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
    
    return elements
   
def build_tree(elements):
    root1 = BinarySearchTreeNode(elements[0]) 
    for i in range(1,len(elements)):
        root1.add_child(elements[i])
    return root1

def build_tree1(elements1):

    root2 = BinarySearchTreeNode(elements1[0])
    
    for i in range(1,len(elements1)):
        root2.add_child(elements1[i])

    return root2

# Defining the function for the good stock portal
def goodstock():
    fileObj = open("C:/Users/New/Downloads/Final Projects/E-Commerce_sales_analysis_using_BST/Productdetails.txt", "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    product = words
    product_tree = build_tree1(product)
    print("GOOD STOCK PORTAL")
    print("\n 1.Add Product \n 2.Open Stock Report \n 3.Search a product \n 4.Sort the Stock \n 5.Remove a Stock \n 6. Back ")
   
    choice = int(input("Enter your choice: "))
    
    if(choice == 1):
        namee = input("Enter Name of Product: ")
        productt = input("Enter Date and time of Product Shipped: ")
        fin_pro = namee+" "+productt
        root1 = BinarySearchTreeNode(fin_pro)
        root1.add_child(fin_pro)
        remember = open("C:/Users/New/Downloads/Final Projects/E-Commerce_sales_analysis_using_BST/Productdetails.txt","a")
        remember.write("\n")
        remember.write(fin_pro)
        remember.close()
        print("Product Added")
        List=[fin_pro]
        with open('C:/Users/New/Downloads/Final Projects/E-Commerce_sales_analysis_using_BST/data.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()
        goodstock()

    elif(choice == 2):
        listToStr = '\n'.join([str(elem) for elem in words])
        print(listToStr)
        print("")
        goodstock()
        
    elif(choice == 3):
        data = input("Enter Product Name: ")
        res = product_tree.search(data)
        if res == True:
            print("Product Present")
        else:
            print("Product not available")
        goodstock() 
        
    elif(choice == 4):
        print("Sorting the Whole tree using Insertion Sort")
        tree2_insertion=insertion_sort(words)
        listToStr1 = '\n'.join([str(elem) for elem in tree2_insertion])
        print(listToStr1)
        print("\n")
        goodstock()
        
    elif(choice == 5):
        deleteitem = input("Enter product to remove: ")
        product_tree.delete(deleteitem)
        print("List updated")
        tree2delete = product_tree.in_order_traversal()
        listToStr1 = '\n'.join([str(elem) for elem in tree2delete])
        print(listToStr1)

        with open("C:/Users/New/Downloads/Final Projects/E-Commerce_sales_analysis_using_BST/Productdetails.txt", "r") as f:
            data = f.readlines()
        with open("C:/Users/New/Downloads/Final Projects/E-Commerce_sales_analysis_using_BST/Productdetails.txt", "a") as f:
            for line in data :
            		if line.strip("\n") != deleteitem :
                            goodstock()

        
    elif(choice == 6):
        mainmenu()
    
        
    else:
        goodstock()
        print("Entered an Invalid Choice")
        

# Defining the function for the Product Purchased Stock portal    
def expstock():
    fileObj = open("C:/Users/New/Downloads/Final Projects/E-Commerce_sales_analysis_using_BST/Productsold.txt", "r") #opens the file in read mode
    exp = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    Productd = exp
    expiry_tree = build_tree(Productd)
        
    print("\nPRODUCT PURCHASED STOCK PORTAL")
    print("\n 1. Print Stock \n 2.Sort product_sold Stock \n 3.Search product \n 4.Back")
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        listToStr = '\n'.join([str(elem) for elem in exp])
        print(listToStr)
        print("")
        expstock()

    elif(choice == 2):
        print("Sorting the Whole tree using Insertion Sort")
        tree2_insertion=insertion_sort(Productd)
        listToStr1 = '\n'.join([str(elem) for elem in tree2_insertion])
        print(listToStr1)
        print("\n")
        expstock()

    elif(choice == 3):
        data = input("Enter product Name: ")
        res = expiry_tree.search(data)
        if res == True:
            print("Product Present")
        else:
            print("Product not available ")
        expstock()

    elif(choice == 4):
        mainmenu()
                
def mainmenu():
    print("HOME ")
    print("************************************************")
    print("*------------AMAZON PRODUCT DETAILS--------------*")
    print("************************************************")
    print(" 1.Good Stock Portal \n 2.Product Purchased Stock Portal \n 3.Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        goodstock()
    elif(choice == 2):
        expstock()
    elif(choice == 3):
        print("************************************************")
        print("              Application closed                ")
        print("              THANK YOU VISIT AGAIN                ")
        print("************************************************")
        sys.exit()
    else:
        print("Input error")
        mainmenu()
           
while True:
    os.system('cls')
    mainmenu()
