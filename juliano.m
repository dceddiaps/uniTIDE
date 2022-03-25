function [jul] = juliano(dia,mes,ano)
%Conversão de um dia no formato dd/mm/aaaa em dia juliano

dias=0;
for i=1:mes-1
    dias(i)=eomday(ano,i);
end

ndias=sum(dias);
jul=ndias+dia;