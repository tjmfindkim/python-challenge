{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Resources\\election_data.csv\n"
     ]
    }
   ],
   "source": [
    "# Modules\n",
    "import os\n",
    "import csv\n",
    "\n",
    "# Set path for file\n",
    "csvpath = os.path.join(\"Resources\", \"election_data.csv\")\n",
    "\n",
    "print (csvpath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes:  3521001\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "# Set variable to 0\n",
    "t_Votes = 0\n",
    "\n",
    "# Open the CSV\n",
    "with open(csvpath, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    csv_header = next(csvreader)\n",
    "       \n",
    "# Loop through looking for the total months\n",
    "    for row in csvreader:\n",
    "            if row[0] != \" \":\n",
    "                t_Votes += 1                           \n",
    "    \n",
    "    print(\"Election Results\")\n",
    "    print(\"-------------------------\")\n",
    "    print(\"Total Votes:  \" + str(t_Votes))\n",
    "    print(\"-------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Khan', 'Li', \"O'Tooley\", 'Correy']\n",
      "[2218231, 492940, 105630, 704200]\n",
      "[0.6300001050837531, 0.13999996023857988, 0.02999999147969569, 0.19999994319797126]\n",
      "range(0, 4)\n"
     ]
    }
   ],
   "source": [
    "# Set variable to 0\n",
    "candidates = []\n",
    "\n",
    "# Open the CSV\n",
    "with open(csvpath, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    csv_header = next(csvreader)\n",
    "       \n",
    "# Create a master list for candidates\n",
    "    for row in csvreader:\n",
    "                candidates.append(row[2])  \n",
    "            \n",
    "# list of candidates - remove duplicate using list(set) and sorted using .sort()\n",
    "candidates_list = list(set(candidates))\n",
    "# candidates_list.sort()\n",
    "# print (candidates_list)\n",
    "\n",
    "# get a vote count for each candidate.\n",
    "candidates_Votes = []\n",
    "for candidate in candidates_list:\n",
    "    candidates_Votes.append(candidates.count(candidate))\n",
    "# print (candidates_Votes)\n",
    "\n",
    "# get a % count for each candidate.\n",
    "candidates_percent = []\n",
    "for candidate in candidates_list:\n",
    "    candidates_percent.append(candidates.count(candidate)/int(t_Votes))\n",
    "# print (candidates_percent)\n",
    "\n",
    "# print (range(len(candidates_list)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Khan: 63.00% 2218231\n",
      "Li: 20.00% 492940\n",
      "O'Tooley: 14.00% 105630\n",
      "Correy: 3.00% 704200\n",
      "['Khan: 63.00% 2218231', 'Li: 20.00% 492940', \"O'Tooley: 14.00% 105630\", 'Correy: 3.00% 704200']\n"
     ]
    }
   ],
   "source": [
    "# print the summary\n",
    "\n",
    "Summary = []\n",
    "\n",
    "for i in range(len(candidates_list)):\n",
    "    print(f\"{candidates_list[i]}: {'{:.2%}'.format(candidates_percent[i])} {candidates_Votes[i]}\")\n",
    "    Summary.append(f\"{candidates_list[i]}: {'{:.2%}'.format(candidates_percent[i])} {candidates_Votes[i]}\")\n",
    "                   \n",
    "# print(Summary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------------------------\n",
      "Winner:    Khan\n",
      "---------------------------\n"
     ]
    }
   ],
   "source": [
    "# find winner\n",
    "winner = max(candidates_percent)\n",
    "w_final = candidates_list[candidates_percent.index(winner)]\n",
    "print(\"---------------------------\")\n",
    "print (f\"Winner:    {w_final}\")\n",
    "print(\"---------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Exporting to .txt file\n",
    "file_txt = open(\"Resources\\output10.txt\", \"w\")\n",
    "\n",
    "\n",
    "file_txt.write(\"Election Results \\n\")\n",
    "file_txt.write(\"------------------------- \\n\")\n",
    "file_txt.write(\"Total Votes:  \" + str(t_Votes) + \"\\n\")\n",
    "file_txt.write(\"------------------------- \\n\")\n",
    "for i in range(len(candidates_list)):\n",
    "    file_txt.write(f\"{candidates_list[i]}: {'{:.2%}'.format(candidates_percent[i])} {candidates_Votes[i]}\" \"\\n\")\n",
    "file_txt.write(\"------------------------- \\n\")\n",
    "file_txt.write(\"Winner:   \" + (w_final) + \"\\n\")\n",
    "file_txt.write(\"------------------------- \\n\")\n",
    "                   #file_txt.write(str(Summary) + \"\\n\")\n",
    "#file_txt.write(\"Greatest Increase in Profits:  \"  +  str(g_date) + \"   $\" + str(g_increase) + \"\\n\")\n",
    "#file_txt.write(\"Greatest Decrease in Profits:  \"  +  str(g_date) + \"   $\" + str(d_increase) + \"\\n\")\n",
    "\n",
    "file_txt.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData]",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
