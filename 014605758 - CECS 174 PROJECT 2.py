#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:44:12 2017

@author: Dominique Oyco dominickoyco@gmail.com
"""
polyesterShirt1 = [0.50, 0.60, 0.75, 0.90, 1.05, 1.20]
polyesterShirt2 = [0.45, 0.55, 0.70, 0.85, 1.00, 1.15]
polyesterShirt3 = [0.40, 0.50, 0.65, 0.80, 0.90, 1.00]
cottonShirt1 = [0.55, 0.65, 0.80, 0.95, 1.10	, 1.25]
cottonShirt2 = [0.50,	0.60,	0.75,	0.90,	1.05,	1.20]
cottonShirt3 = [0.45,	0.55,	0.70,	0.85,	0.95,	1.05]

#ASK THE USER IF THEY WANT TO BUY SHIRTS OR NOT
polyester_input = input("Do you want to buy polyester shirts? (Y/N): ")
cotton_input = input("Do you want to buy cotton shirts? (Y/N): ")

#ASK THE USER FOR MORE INPUTS
if polyester_input == 'Y':
    polyester_xs_quantity = int(input("How many XS size shirts do you want? "))
    polyester_s_quantity = int(input("How many S size shirts do you want? "))
    polyester_m_quantity = int(input("How many M size shirts do you want? "))
    polyester_l_quantity = int(input("How many L size shirts do you want? "))
    polyester_xl_quantity = int(input("How many XL size shirts do you want? "))
    polyester_xxl_quantity = int(input("How many XXL size shirts do you want? "))
    if polyester_xs_quantity <= 100:
        polyester_xs_order = polyesterShirt1[0] * polyester_xs_quantity
    elif polyester_xs_quantity > 100 and polyester_xs_quantity <= 200:
        polyester_xs_order = polyesterShirt2[0] * polyester_xs_quantity
    elif polyester_xs_quantity > 200:
        polyester_xs_order = polyesterShirt3[0] * polyester_xs_quantity
    else:
        polyester_xs_order = 0
    if polyester_s_quantity <= 100:
        polyester_s_order = polyesterShirt1[1] * polyester_s_quantity
    elif polyester_s_quantity > 100 and polyester_s_quantity <= 200:
        polyester_s_order = polyesterShirt2[1] * polyester_s_quantity
    elif polyester_s_quantity > 200:
        polyester_s_order = polyesterShirt3[1] * polyester_s_quantity
    else:
        polyester_s_order = 0
    if polyester_m_quantity <= 100:
        polyester_m_order = polyesterShirt1[2] * polyester_m_quantity
    elif polyester_m_quantity > 100 and polyester_m_quantity <= 200:
        polyester_m_order = polyesterShirt2[2] * polyester_m_quantity
    elif polyester_m_quantity > 200:
        polyester_m_order = polyesterShirt3[2] * polyester_m_quantity
    else:
        polyester_m_order = 0
    if polyester_l_quantity <= 100:
        polyester_l_order = polyesterShirt1[3] * polyester_l_quantity
    elif polyester_l_quantity > 100 and polyester_l_quantity <= 200:
        polyester_l_order = polyesterShirt2[3] * polyester_l_quantity
    elif polyester_l_quantity > 200:
        polyester_l_order = polyesterShirt3[3] * polyester_l_quantity
    else:
        polyester_l_order = 0
    if polyester_xl_quantity <= 100:
        polyester_xl_order = polyesterShirt1[4] * polyester_xl_quantity
    elif polyester_xl_quantity > 100 and polyester_xl_quantity <= 200:
        polyester_xl_order = polyesterShirt2[4] * polyester_xl_quantity
    elif polyester_xl_quantity > 200:
        polyester_xl_order = polyesterShirt3[4] * polyester_xl_quantity
    else:
        polyester_xl_order = 0
    if polyester_xxl_quantity <= 100:
        polyester_xxl_order = polyesterShirt1[5] * polyester_xxl_quantity
    elif polyester_xxl_quantity > 100 and polyester_xs_quantity <= 200:
        polyester_xxl_order = polyesterShirt2[5] * polyester_xxl_quantity
    elif polyester_xxl_quantity > 200:
        polyester_xxl_order = polyesterShirt3[5] * polyester_xxl_quantity
    else:
        polyester_xxl_order = 0
    polyester_order_total = float(polyester_xs_order + polyester_s_order + polyester_m_order 
                    + polyester_l_order + polyester_xl_order + polyester_xxl_order)
    print("Your order total is: $ %.2f" % polyester_order_total)
elif polyester_input == 'N':
    if cotton_input == 'Y':
        cotton_xs_quantity = int(input("How many XS size shirts do you want? "))
        cotton_s_quantity = int(input("How many S size shirts do you want? "))
        cotton_m_quantity = int(input("How many M size shirts do you want? "))
        cotton_l_quantity = int(input("How many L size shirts do you want? "))
        cotton_xl_quantity = int(input("How many XL size shirts do you want? "))
        cotton_xxl_quantity = int(input("How many XXL size shirts do you want? "))
        if cotton_xs_quantity <= 100:
            cotton_xs_order = cottonShirt1[0] * cotton_xs_quantity
        elif cotton_xs_quantity > 100 and cotton_xs_quantity <= 200:
            cotton_xs_order = cottonShirt2[0] * cotton_xs_quantity
        elif cotton_xs_quantity > 200:
            cotton_xs_order = cottonShirt3[0] * cotton_xs_quantity
        else:
            cotton_xs_order = 0
        if cotton_s_quantity <= 100:
            cotton_s_order = cottonShirt1[1] * cotton_s_quantity
        elif cotton_s_quantity > 100 and cotton_s_quantity <= 200:
            cotton_s_order = cottonShirt2[1] * cotton_s_quantity
        elif cotton_s_quantity > 200:
            cotton_s_order = cottonShirt3[1] * cotton_s_quantity
        else:
            cotton_s_order = 0
        if cotton_m_quantity <= 100:
            cotton_m_order = cottonShirt1[2] * cotton_m_quantity
        elif cotton_m_quantity > 100 and cotton_m_quantity <= 200:
            cotton_m_order = cottonShirt2[2] * cotton_m_quantity
        elif cotton_m_quantity > 200:
            cotton_m_order = cottonShirt3[2] * cotton_m_quantity
        else:
            cotton_m_order = 0
        if cotton_l_quantity <= 100:
            cotton_l_order = cottonShirt1[3] * cotton_l_quantity
        elif cotton_l_quantity > 100 and cotton_l_quantity <= 200:
            cotton_l_order = cottonShirt2[3] * cotton_l_quantity
        elif cotton_l_quantity > 200:
            cotton_l_order = cottonShirt3[3] * cotton_l_quantity
        else:
            cotton_l_order = 0
        if cotton_xl_quantity <= 100:
            cotton_xl_order = cottonShirt1[4] * cotton_xl_quantity
        elif cotton_xl_quantity > 100 and cotton_xl_quantity <= 200:
            cotton_xl_order = cottonShirt2[4] * cotton_xl_quantity
        elif cotton_xl_quantity > 200:
            cotton_xl_order = cottonShirt3[4] * cotton_xl_quantity
        else:
            cotton_xl_order = 0
        if cotton_xxl_quantity <= 100:
            cotton_xxl_order = cottonShirt1[5] * cotton_xxl_quantity
        elif cotton_xxl_quantity > 100 and cotton_xs_quantity <= 200:
            cotton__xxl_order = cottonShirt2[5] * cotton_xxl_quantity
        elif cotton_xxl_quantity > 200:
            cotton_xxl_order = cottonShirt3[5] * cotton_xxl_quantity
        else:
            cotton_xxl_order = 0

        cotton_order_total = float(cotton_xs_order + cotton_s_order + cotton_m_order 
                    + cotton_l_order + cotton_xl_order + cotton_xxl_order)
        print("Your order total is: $ %.2f" % cotton_order_total)
    elif cotton_input == 'N': 
        print("goodbye")
else:
    print("goodbye")

##POLYESTER SHIRT ORDER
#    
##XS QUANTITY
#if polyester_xs_quantity <= 100:
#    polyester_xs_order = 0.50 * polyester_xs_quantity
#elif polyester_xs_quantity > 100 and polyester_xs_quantity <= 200:
#    polyester_xs_order = 0.45 * polyester_xs_quantity
#elif polyester_xs_quantity > 200:
#    polyester_xs_order = 0.40 * polyester_xs_quantity
#else:
#    polyester_xs_order = 0
#    
##S QUANTITY
#if polyester_s_quantity <= 100:
#    polyester_s_order = 0.60 * polyester_s_quantity
#elif polyester_s_quantity > 100 and polyester_s_quantity <= 200:
#    polyester_s_order = 0.55 * polyester_s_quantity
#elif polyester_s_quantity > 200:
#    polyester_s_order = 0.50 * polyester_s_quantity
#else:
#    polyester_s_order = 0
#    
##M QUANTITY
#if polyester_m_quantity <= 100:
#    polyester_m_order = 0.75 * polyester_m_quantity
#elif polyester_m_quantity > 100 and polyester_m_quantity <= 200:
#    polyester_m_order = 0.70 * polyester_m_quantity
#elif polyester_m_quantity > 200:
#    polyester_m_order = 0.65 * polyester_m_quantity
#else:
#    polyester_m_order = 0
#    
##L QUANTITY
#if polyester_l_quantity <= 100:
#    polyester_l_order = 0.90 * polyester_l_quantity
#elif polyester_l_quantity > 100 and polyester_l_quantity <= 200:
#    polyester_l_order = 0.85 * polyester_l_quantity
#elif polyester_l_quantity > 200:
#    polyester_l_order = 0.80 * polyester_l_quantity
#else:
#    polyester_l_order = 0
#    
##XL QUANTITY
#if polyester_xl_quantity <= 100:
#    polyester_xl_order = 1.10 * polyester_xl_quantity
#elif polyester_xl_quantity > 100 and polyester_xl_quantity <= 200:
#    polyester_xl_order = 1.05 * polyester_xl_quantity
#elif polyester_xl_quantity > 200:
#    polyester_xl_order = 0.95 * polyester_xl_quantity
#else:
#    polyester_xl_order = 0
#    
##XXL QUANTITY    
#if polyester_xxl_quantity <= 100:
#    polyester_xxl_order = 1.25 * polyester_xxl_quantity
#elif polyester_xxl_quantity > 100 and polyester_xs_quantity <= 200:
#    polyester_xxl_order = 1.20 * polyester_xxl_quantity
#elif polyester_xxl_quantity > 200:
#    polyester_xxl_order = 1.05 * polyester_xxl_quantity
#else:
#    polyester_xxl_order = 0
#
##CALCULATE THE TOTAL ORDER AMOUNT
#polyester_order_total = float(polyester_xs_order + polyester_s_order + polyester_m_order 
#                    + polyester_l_order + polyester_xl_order + polyester_xxl_order)
#print("Your order total is: $ %.2f" % polyester_order_total)

#COTTON SHIRT ORDER
    
##XS QUANTITY
#if cotton_xs_quantity <= 100:
#    cotton_xs_order = 0.50 * cotton_xs_quantity
#elif cotton_xs_quantity > 100 and cotton_xs_quantity <= 200:
#    cotton_xs_order = 0.45 * cotton_xs_quantity
#elif cotton_xs_quantity > 200:
#    cotton_xs_order = 0.40 * cotton_xs_quantity
#else:
#    cotton_xs_order = 0
#    
##S QUANTITY
#if cotton_s_quantity <= 100:
#    cotton_s_order = 0.60 * cotton_s_quantity
#elif cotton_s_quantity > 100 and cotton_s_quantity <= 200:
#    cotton_s_order = 0.55 * cotton_s_quantity
#elif cotton_s_quantity > 200:
#    cotton_s_order = 0.50 * cotton_s_quantity
#else:
#    cotton_s_order = 0
#    
##M QUANTITY
#if cotton_m_quantity <= 100:
#    cotton_m_order = 0.75 * cotton_m_quantity
#elif polyester_m_quantity > 100 and cotton_m_quantity <= 200:
#    cotton_m_order = 0.70 * cotton_m_quantity
#elif polyester_m_quantity > 200:
#    cotton_m_order = 0.65 * cotton_m_quantity
#else:
#    cotton_m_order = 0
#    
##L QUANTITY
#if cotton_l_quantity <= 100:
#    cotton_l_order = 0.90 * cotton_l_quantity
#elif cotton_l_quantity > 100 and cotton_l_quantity <= 200:
#    cotton_l_order = 0.85 * cotton_l_quantity
#elif cotton_l_quantity > 200:
#    cotton_l_order = 0.80 * cotton_l_quantity
#else:
#    cotton_l_order = 0
#    
##XL QUANTITY
#if cotton_xl_quantity <= 100:
#    cotton_xl_order = 1.10 * cotton_xl_quantity
#elif cotton_xl_quantity > 100 and cotton_xl_quantity <= 200:
#    cotton_xl_order = 1.05 * cotton_xl_quantity
#elif cotton_xl_quantity > 200:
#    cotton_xl_order = 0.95 * cotton_xl_quantity
#else:
#    cotton_xl_order = 0
#    
##XXL QUANTITY    
#if cotton_xxl_quantity <= 100:
#    cotton_xxl_order = 1.25 * cotton_xxl_quantity
#elif cotton_xxl_quantity > 100 and cotton_xs_quantity <= 200:
#    cotton__xxl_order = 1.20 * cotton_xxl_quantity
#elif cotton_xxl_quantity > 200:
#    cotton_xxl_order = 1.05 * cotton_xxl_quantity
#else:
#    cotton_xxl_order = 0
#
##CALCULATE THE TOTAL ORDER AMOUNT
#cotton_order_total = float(cotton_xs_order + cotton_s_order + cotton_m_order 
#                    + cotton_l_order + cotton_xl_order + cotton_xxl_order)
#print("Your order total is: $ %.2f" % cotton_order_total)
