{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3effb6fe",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n",
      "My name is HAL!\n",
      "What is your name?\n",
      "Alexi Musick\n",
      "Hello Alexi Musick nice to meet you!\n"
     ]
    }
   ],
   "source": [
    "#prints out a string\n",
    "print('Hello World!\\nMy name is HAL!\\nWhat is your name?')\n",
    "\n",
    "#Asks for user's name using input() function\n",
    "def check_for_name(name):\n",
    "    if name.strip().isdigit():\n",
    "        print(\"Please enter your name not a number.\")\n",
    "        username = input('')\n",
    "        check_for_name(username)\n",
    "    else:\n",
    "        print('Hello '+name+' nice to meet you!')\n",
    "username = input('')\n",
    "check_for_name(username)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45b9f73a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
