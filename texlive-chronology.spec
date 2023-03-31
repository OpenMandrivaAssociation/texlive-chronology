Name:		texlive-chronology
Version:	37934
Release:	2
Summary:	Provides a horizontal timeline
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chronology
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chronology.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chronology.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/chronology
%doc %{_texmfdistdir}/doc/latex/chronology

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
