% IH - Divisão de Oceanografia
% Seção de Marés
% Data: 05/02/2014
% Programa QC1_CONTINENTE.M
% Efectua um controlo de qualidade de nível 1 (aplicado a tempo real) aos
% dados. Controlo apenas em altura e que efetua os seguinte testes:
% -Out of range values
% -Statibility test
% -Outliers
% São colocadas Flags nos dados de acordo com a seguinte correspondencia:
% 1 - Good
% 4 - Bad
% É determinado o nº de registos em falta, face ao período de observação,e 
% o nº de registos com flag=3,4. 

clear all

disp('  ')
disp('********************************************************************')
disp('                        QC1 - CONTINENTE')

% Abre o ficheiro do Vega 
[filename,path]=uigetfile('*.*','Selecione o ficheiro');
cd(path)
fid=fopen(filename,'r');
dad=fscanf(fid,'%4d-%2d-%2d %2d:%2d:%2d %g %g %g',[9 inf]);dad=dad';
fclose(fid);
SN=datenum(dad(:,1),dad(:,2),dad(:,3),dad(:,4),dad(:,5),dad(:,6));
ano1=dad(1,1);
cod=dad(1,8);
codstr=num2str(cod,'%03d');
idmareg=dad(1,9);
idmaregstr=num2str(idmareg,'%03d');
x=SN-datenum(ano1-1,12,31,0,0,0);
y=dad(:,7); %Dados já são recebidos ao ZH
clear filename fid path


% Determina o nº de registos esperados e o nº de registos recebidos
% Para o nº de registos esperados são considerados dias completos (24h)

T=length(y); %nº de registos recebidos

mes1=dad(1,2);
dia1=dad(1,3);
jul1=juliano(dia1,mes1,ano1);
ano2=dad(end,1);
mes2=dad(end,2);
dia2=dad(end,3);
jul2=juliano(dia2,mes2,ano2);

if jul2<jul1
    ib=ibisst(ano1);
    if ib==1
        d=366;
    elseif ib==0
        d=365;
    end
    ndias=((d-jul1)+1)+jul2;
elseif jul2>jul1
    ndias=(jul2-jul1)+1;
elseif jul2==jul1
    ndias=1;
end
regT=ndias*24*60; %nº de registos esperados

disp(['Código do porto: ',codstr])
disp(['ID do marégrafo: ',idmaregstr])
disp(['Nº registos esperados = ',num2str(regT)])
disp(['Nº registos recebidos = ',num2str(T)])


% Teste de Controlo de Qualidade em altura

flag=ones(T,1); %Coloca Flag=1 em todos os dados recebidos

% Out of range values (Flag=4)
Liminf=-0.5;
Limsup=5;
for j=1:T
    if y(j)<Liminf || y(j)>Limsup
        flag(j)=4;
    end
end

% % Statibility test (Flag=4)
% for k=11:T-10
%     if y(k)<Liminf || y(k)>Limsup
%         flag(k)=4;
%     end
% end

% Outliers (Flag=4)
% dif=2;
% for l=2:T-1
%     if (y(l)-y(l-1))>dif
%         flag(l)=3;
%         %flag(l-1)=3;
%     end
% end

y1=0; x1=0; SN1=0; 
n=1;
for m=1:T
    if flag(m)==1
        y1(n)=y(m);
        SN1(n)=SN(m);
        x1(n)=x(m);
        n=n+1;
    end
end
T1=length(y1);
disp(['Nº registos aceites no controlo em altura = ',num2str(T1)])

y4=0; x4=0; SN4=0; flag4=0;
n=1;
for o=1:T
    if flag(o)==4
        y4(n)=y(o);
        SN4(n)=SN(o);
        x4(n)=x(o);
        flag4(n)=flag(o);
        n=n+1;
    end
end
T4=length(y4);


% Grafica os dados
figure
plot(x,y,'k')
title(['COD=',codstr,' IDmareg=',idmaregstr])
xlabel(['Dias de ',num2str(ano1)])
ylabel('Altura de água ao ZH (m)')

%Grafica os dados
figure
plot(x1,y1,'.k')
title(['COD=',codstr,' IDmareg=',idmaregstr])
xlabel(['Dias de ',num2str(ano1)])
ylabel('Altura de água ao ZH (m)')

if y4~=0
    hold on
    plot(x4,y4,'.r')
end
hold off

SN4str=datestr(SN4,31);
fid=fopen(['Relatorio_',codstr,'_',idmaregstr,'.txt'],'w'); 
fprintf(fid,'Código do porto: %3s\n',codstr);
fprintf(fid,'ID do marégrafo: %3s\n',idmaregstr);
fprintf(fid,'Nº registos esperados = %10s\n',num2str(regT));
fprintf(fid,'Nº registos recebidos = %10s\n',num2str(T));
fprintf(fid,'Nº registos aceites no controlo em altura = %10s\n',num2str(T1));
fprintf(fid,'Anomalias:\n');
if y4~=0
    for i=1:T4
        fprintf(fid,'%19s %10.6f %9.6f %2d\n',SN4str(i,:),x4(i),y4(i),flag4(i));
    end
end
if y4==0
    fprintf(fid,'Nenhuma\n');
end    
fclose(fid);
disp('FIM')

% fid=fopen(['obs',codstr,'_',codmaregstr,'.txt'],'w'); 
% fprintf(fid,'GDH# Altura# TipoFen# Flag Qualidade# Flag Recepção# ID Maregrafo# Codigo do porto# Nsampling# Valor Bruto# Observações#\n');
% for i=1:T
%     fprintf(fid,'%19s#%11.6f#%3d#%3d#%3d#%5d#%5d#\n',SNstr(i,:),y(i),tfen,flagQ,flagR,codmareg,cod);
% end
% fclose(fid);
% disp('O programa terminou! Pode consultar o novo ficheiro.')
