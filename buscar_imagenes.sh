#!/bin/bash
for i in {1..46}; do
	md5=$(md5sum imagen$i.jpg | awk '{ print $1 }')
	if [ "$md5" == "e5ed313192776744b9b93b1320b5e268" ]; then
		echo "El archivo que coincide es : imagen$i.jpg"
	fi
	done
	
