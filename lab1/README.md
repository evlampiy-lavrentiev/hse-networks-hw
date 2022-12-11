## Топология

![](images/topology.jpg)

## Конфигурация
Все конфигурационные файлы лежат в папке `configs/`

## Ping VPC1 —> VPC2
![](images/ping1.jpg)
## VPC2
![](images/vpc2.jpg)
## Ping VPC2 —> VPC1
![](images/ping2.jpg)

## Отказоустойчивость
При отключении интерфейса `L2left - L2_root` или `L2left - L2right` пинги всё равно успешно доходят

![](images/reliable-ping.jpg)