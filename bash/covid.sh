#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITAL=$(echo $DATA | jq '.[0].hospitalizedCumulative')
TODAY=$(date)

echo " "
echo "On $TODAY," 
echo "COVID update - there were:" 
echo "$POSITIVE positive cases" 
echo "$NEGATIVE negative tests" 
echo "$DEATHS deaths" 
echo "$HOSPITAL hospitalized"
echo " "
