for i in {0..$1}; do wget $2/bg$(python2 -c "print hex($i)[2:]").png -O $(python2 -c "print '$i'.zfill(4)").png; done
convert *.png $3.pdf
