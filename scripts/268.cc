#include <primecount.hpp>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <string>

std::vector<int> sieve(int n){
    std::vector<char> f(n+1,1);
    std::vector<int> p;
    f[0]=f[1]=0;
    for(int i=2;i<=n;++i)if(f[i]){
        p.push_back(i);
        for(int j=i*2;j<=n;j+=i)f[j]=0;
    }
    return p;
}

void bar(const std::string& name,std::size_t cur,std::size_t tot){
    static const int W=40;
    double r=double(cur)/tot;
    int filled=r*W;
    std::cerr<<"\r"<<name<<" ["<<std::string(filled,'=')<<std::string(W-filled,' ')<<"] "
            <<int(r*100)<<"% ("<<cur<<'/'<<tot<<")"<<std::flush;
    if(cur==tot)std::cerr<<'\n';
}

int main(){
    // constexpr long long N=10000000000000000LL;
    constexpr long long N=1000000;
    const auto primes=sieve(100);

    long long T=1+primecount::pi(N)-primecount::pi(100);
    auto gr=[&](int p){return int(std::log((long double)N)/std::log((long double)p))+1;};

    std::size_t done=0,total=primes.size();
    for(int p1:primes){
        for(int k1=1;k1<gr(p1);++k1){
            long long num=std::pow(p1,k1);
            if(num>N)break;
            long long kk=N/num;
            T+=kk<100?1:1+primecount::pi(kk)-primecount::pi(100);
        }
        bar("1-prime ",++done,total);
    }

    total=primes.size()*(primes.size()-1)/2;
    done=0;
    for(std::size_t i=0;i<primes.size();++i){
        for(std::size_t j=i+1;j<primes.size();++j){
            for(int k1=1;k1<gr(primes[i]);++k1)
                for(int k2=1;k2<gr(primes[j]);++k2){
                    long long num=std::pow(primes[i],k1)*std::pow(primes[j],k2);
                    if(num>N)break;
                    long long kk=N/num;
                    T+=kk<100?1:1+primecount::pi(kk)-primecount::pi(100);
                }
            bar("2-prime ",++done,total);
        }
    }

    total=primes.size()*(primes.size()-1)*(primes.size()-2)/6;
    done=0;
    for(std::size_t i=0;i<primes.size();++i){
        for(std::size_t j=i+1;j<primes.size();++j){
            for(std::size_t k=j+1;k<primes.size();++k){
                for(int k1=1;k1<gr(primes[i]);++k1)
                    for(int k2=1;k2<gr(primes[j]);++k2)
                        for(int k3=1;k3<gr(primes[k]);++k3){
                            long long num=std::pow(primes[i],k1)*std::pow(primes[j],k2)*std::pow(primes[k],k3);
                            if(num>N)break;
                            long long kk=N/num;
                            T+=kk<100?1:1+primecount::pi(kk)-primecount::pi(100);
                        }
                bar("3-prime ",++done,total);
            }
        }
    }

    std::cout<<N-T<<'\n';
}
