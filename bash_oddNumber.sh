#Use for loops to display only odd natural numbers from  0 to 99. There is no input

#!/bin/bash
#for <elements> in <lists>
#do
#   <commands>
#done



for i in {1..99}
do
    if [[ $i%2 -eq 0 ]]
    then
        continue
    fi
    echo $i
done