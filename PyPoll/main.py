{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Modules\n",
    "import os\n",
    "import csv\n",
    "\n",
    "# Set path for file\n",
    "csvpath = os.path.join(\"Resources\", \"election_data.csv\")\n",
    "\n",
    "\n",
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
    "    #print(\"Election Results\")\n",
    "    #print(\"-------------------------\")\n",
    "    #print(\"Total Votes:  \" + str(t_Votes))\n",
    "    #print(\"-------------------------\")\n",
    "    \n",
    "\n",
    "    \n",
    "# Create a master list for candidates\n",
    "candidates = []\n",
    "for row in csvreader:\n",
    "    candidates.append(row[2])  \n",
    "            \n",
    "# list of candidates - remove duplicate using list(set)\n",
    "candidates_list = list(set(candidates))\n",
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
    "\n",
    "\n",
    "Summary = []\n",
    "\n",
    "for i in range(len(candidates_list)):\n",
    "    print(f\"{candidates_list[i]}: {'{:.2%}'.format(candidates_percent[i])} {candidates_Votes[i]}\")\n",
    "    \n",
    "                   \n",
    "# find winner\n",
    "winner = max(candidates_percent)\n",
    "w_final = candidates_list[candidates_percent.index(winner)]\n",
    "print(\"---------------------------\")\n",
    "print (f\"Winner:    {w_final}\")\n",
    "print(\"---------------------------\")\n",
    "                   \n",
    "                   #Exporting to .txt file\n",
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
