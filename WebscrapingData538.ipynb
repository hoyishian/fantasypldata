{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Helper function used in extractNamesFromMainPage()\n",
    "def hasNumbers(inputString):\n",
    "    return any(char.isdigit() for char in inputString)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Extract team names from 538 Main Page\n",
    "def extractNamesFromMainPage():\n",
    "    URL = \"https://projects.fivethirtyeight.com/soccer-predictions/premier-league/\"\n",
    "    r = requests.get(URL) \n",
    "    soup = BeautifulSoup(r.content, 'html5lib') \n",
    "    \n",
    "    table = soup.findAll('div', attrs = {'class':'name'})\n",
    "    \n",
    "    teams = []\n",
    "    for row in soup.findAll('div', attrs = {'class':'name'}):\n",
    "        team = row.text\n",
    "        if(hasNumbers(team)):\n",
    "            continue\n",
    "        else:\n",
    "            teams.append(team)\n",
    "    \n",
    "    teams = list(set(teams))\n",
    "    return sorted(teams)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Arsenal',\n",
       " 'Aston Villa',\n",
       " 'Bournemouth',\n",
       " 'Brighton',\n",
       " 'Burnley',\n",
       " 'Chelsea',\n",
       " 'Crystal Palace',\n",
       " 'Everton',\n",
       " 'Leicester',\n",
       " 'Liverpool',\n",
       " 'Man. City',\n",
       " 'Man. United',\n",
       " 'Newcastle',\n",
       " 'Norwich',\n",
       " 'Sheffield Utd',\n",
       " 'Southampton',\n",
       " 'Tottenham',\n",
       " 'Watford',\n",
       " 'West Ham',\n",
       " 'Wolves']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "extractNamesFromMainPage()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
