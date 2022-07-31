qselect -u yairdaon | xargs qdel
declare -a ARR=("-0.5" "0" "0.5" "1")
rm -rvf output/*
for ID in {0..2}; do
    echo "Create and run waning/scripts/run$ID script."
    echo "#!/bin/bash" > scripts/run$ID.sh
    echo "cd waning/" >> scripts/run$ID.sh
    echo "module load miniconda/miniconda3-4.7.12-environmentally" >> scripts/run$ID.sh
    echo "conda activate YairDaon" >> waning/scripts/run$ID.sh

    for EPS in ${ARR[@]}; do
	echo "time python main.py $ID 01 $EPS" >> scripts/run$ID.sh
	echo "time python main.py $ID 10 $EPS" >> scripts/run$ID.sh
    done
    echo "conda deactivate" >> scripts/run$ID.sh
    qsub -q uriobols -lnodes=1:ppn=36 scripts/run$ID.sh
done

sleep 5
qstat -u yairdaon
