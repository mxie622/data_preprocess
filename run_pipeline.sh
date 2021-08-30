# n=0;while(($n<=10));do top -n 1;n=$((n + 1));sleep 2;done
set -ex
python ./python/exec/process_image.py