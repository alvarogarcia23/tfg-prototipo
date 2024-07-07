#! /bin/bash

pushd ./basemaps

for i in default google michelin bing bw
do
	sed -e "s/STYLE = default/STYLE = $i/g" ./settings.mk > ./settings-prepared.mk
	make clean
	make -f ./settings-prepared.mk
done

popd
