Name:		texlive-stringenc
Version:	52982
Release:	1
Summary:	Converting a string between different encodings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stringenc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stringenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stringenc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stringenc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides \StringEncodingConvert for converting a
string between different encodings. Both LaTeX and plain-TeX
are supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/stringenc
%{_texmfdistdir}/tex/generic/stringenc
%doc %{_texmfdistdir}/doc/latex/stringenc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
