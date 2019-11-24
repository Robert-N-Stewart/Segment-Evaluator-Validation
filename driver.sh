#see readme.txt for directions (must pass log files)
cat $2 | head -10000 | sed -n 's/.*evaluated: \([[:alnum:]]*\).*\[\(.*\)\]/\1, \2/p' > cleaned-evaluator-integration.txt
cat $1 | head -10000 | sed -n 's/.*evaluated: \([[:alnum:]]*\).*\[\(.*\)\]/\1, \2/p' > cleaned-evaluator-integration-baseline.txt

python compareLogs.py

rm cleaned-evaluator-integration.txt
rm cleaned-evaluator-integration-baseline.txt