%IBISST - diz se o ano � bissexto
%         output =1  se o ano � bissexto
%                =0  se o ano � comum 
%         o ano tem de ser dado com 4 algarismos

function diasup = ibisst (ano)

if mod(ano,400) == 0,
   diasup = 1;
elseif mod(ano,100) == 0,
   diasup = 0;
elseif mod(ano,4) == 0,
   diasup = 1;
else
   diasup = 0;
end

      