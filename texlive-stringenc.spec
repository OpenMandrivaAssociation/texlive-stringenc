%global tl_name stringenc
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.12
Release:	%{tl_revision}.1
Summary:	Converting a string between different encodings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stringenc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stringenc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stringenc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stringenc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides \StringEncodingConvert for converting a string
between different encodings. Both LaTeX and plain-TeX are supported.

