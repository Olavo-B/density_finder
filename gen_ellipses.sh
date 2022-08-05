# clear files
echo -e 'image, manual_count' >'misc/manual_count/val.txt' 
echo -e 'image, manual_count' >'misc/manual_count/train.txt'

# process files
echo "Processing Training images"
for FILE in misc/wheat_ears_counting_dataset/train/labels/*; 
    do 
        echo -n "  -- $(basename "$FILE")"; 
        python3 main.py $FILE;
        echo " ok"
    done

echo -e "\nProcessing Validation images"
for FILE in misc/wheat_ears_counting_dataset/val/labels/*; 
    do 
        echo -n "  -- $(basename "$FILE")"; 
        python3 main.py $FILE;
        echo " ok"
    done