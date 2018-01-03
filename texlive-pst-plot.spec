Name:		texlive-pst-plot
Version:	1.87
Release:	1
Summary:	Plot data using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-plot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-plot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-plot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides plotting of data (typically from external
files), using PSTricks. Plots may be configured using a wide
variety of parameters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-plot
%{_texmfdistdir}/tex/latex/pst-plot
%doc %{_texmfdistdir}/doc/generic/pst-plot

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
