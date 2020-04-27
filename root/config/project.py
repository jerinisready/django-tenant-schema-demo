"""
Site can act in many ways ways:

Brand          -------------------------------------------------------->     Dealer
Wholesaler     -------------------------------------------------------->     Dealer
Brand          ----------->          Executive              ----------->     Dealer
Brand          ----------->          Wholesaler             ----------->     Dealer
Wholesaler     ----------->          Executive              ----------->     Dealer


if there is a middlemen; make {UTSAV_HAVE_MIDDLEMEN = TRUE}
if there is a middlemen; and when he have to recommend all the invoices make {UTSAV_MIDDLEMEN_MUST_APPROVE = TRUE}

{UTSAV_PROGRAMME} is the Short Name of the Project
{UTSAV_NAME} is the Full Name of the Programme
{UTSAV_LENGTHY_LOGO} is the Wide Logo of the Programme
{UTSAV_ICON} is the Logo Icon of the Programme
{UTSAV_MIDDLEMEN_LABEL} is the name called for middlemen
{UTSAV_DEALER_LABEL} is the name called for dealer

"""

UTSAV_SELF_LABEL = 'Buildware'
UTSAV_PROGRAMME = "Celerbrate"
UTSAV_NAME = "Buildware Celerbrate"
UTSAV_LENGTHY_LOGO = "ahana/custom/logo.png"
UTSAV_ICON = "ahana/img/icons/logo-icon.png"

UTSAV_HAVE_MIDDLEMEN = False
UTSAV_MIDDLEMEN_MUST_APPROVE = UTSAV_HAVE_MIDDLEMEN and False
UTSAV_DEDICATED_OUR_PRICE = False

UTSAV_MIDDLEMEN_LABEL = ('Wholesaler', 'Executive', 'Distributor')[1]
UTSAV_DEALER_LABEL = 'Dealer'



