#!/bin/bash

echo -e "Creating Helmchart manifests"
python3 extras/substitution.py
ls templates/cluster-register.yaml
if [[ $? == 0 ]]; then
	echo -e "Helmchart manifest created successfully"
else
	echo -e "Issue in Helmchart manifest creation"
fi
