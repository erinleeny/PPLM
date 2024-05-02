#!/bin/bash

strings=("In summary" "This essay discusses" "Views on" "The connection" "Foundational to this is" "To review," "In brief," "An illustration of" "Furthermore," "The central theme" "To conclude," "The key aspect" "Prior to this" "Emphasised are" "To summarise" "The relationship" "More importantly," "It has been shown" "The issue focused on" "In this essay")
files=("legal" "politics" "religion" "science" "technology")

for file in "${files[@]}"
do
    for str in "${strings[@]}"
    do
        python run_pplm_SSE.py -B $file --cond_text "$str" --length 50 --gamma 1.5 --num_iterations 3 --num_samples 1 --stepsize 0.01 --window_length 5 --kl_scale 0.01 --gm_scale 0.99 --verbosity "quiet" >> "pplm_${file}.txt"
    done
done
