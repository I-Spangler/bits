#include<iostream>
#include<string>
#include<cstdlib>

using namespace std;
class calendario{
  private:
    int dia;
    int mes;
    int ano;
    bool valida(int dia, int mes){
      if(dia > 31 || mes > 12 || dia < 1 || mes < 1){
        cout<<"Erro: data inválida. Insira outra data.\n";
        return false;
      }
      if(dia >= 30 && mes == 2){
        cout<<"Erro: data inválida. Insira outra data.";
        return false;
      }
      if(dia >= 31 && (mes == 4 || mes == 6 || mes == 9 || mes == 11)){
        cout<<"Erro: data inválida. Insira outra data.";
        return false;
      }
      return true;
    }
  public:
    void scanData(){
    cout<<"Insira a data: (dd mm aaaa)";
      cin>>dia>>mes>>ano;
      if(valida(dia, mes) == false)
        scanData();
    }
    int calculaDia(){
      int bissexto = ano/4;
      return (ano-1)*365 + bissexto + (mes-1)*30 + dia;
    }
    int calculaMes(){
      return (ano-1)*12 + mes;
    }
    int calculaAno(){
      return ano;
    }
 };

int main(){
  calendario data1, data2;
  data1.scanData();
  data2.scanData();
  cout<<"O número de dias é:"<<abs(data1.calculaDia() - data2.calculaDia())<<"\n";
  cout<<"O número de meses é:"<<abs(data1.calculaMes() - data2.calculaMes())<<"\n";
  cout<<"O número de anos é:"<<abs(data1.calculaAno() - data2.calculaAno())<<"\n";
}
