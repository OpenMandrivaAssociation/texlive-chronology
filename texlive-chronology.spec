# revision 18994
# category Package
# catalog-ctan /macros/latex/contrib/chronology
# catalog-date 2010-06-15 10:45:39 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-chronology
Version:	1.0
Release:	2
Summary:	Provides a horizontal timeline
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chronology
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chronology.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chronology.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chronology.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A timeline package that allows labelling of events with per-day
granularity. Other features include relative positioning with
unit specification, adjustable tick mark step size, and scaling
to specified width.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chronology/chronology.sty
%doc %{_texmfdistdir}/doc/latex/chronology/README
%doc %{_texmfdistdir}/doc/latex/chronology/README.txt
%doc %{_texmfdistdir}/doc/latex/chronology/chronology.hd
%doc %{_texmfdistdir}/doc/latex/chronology/chronology.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chronology/chronology.dtx
%doc %{_texmfdistdir}/source/latex/chronology/chronology.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
