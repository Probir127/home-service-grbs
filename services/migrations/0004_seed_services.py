from django.db import migrations
from django.utils.text import slugify


SERVICES = [
    # Privata tjänster
    {
        "title": "Hemstädning",
        "category": "private",
        "subtitle": "Regelbunden städning av ditt hem",
        "short_description": "Vi håller ditt hem rent och fräscht med regelbunden och professionell städning.",
        "description": "Vår hemstädning är anpassad efter dina behov och önskemål. Vi använder miljövänliga rengöringsmedel och ser till att varje hörn i ditt hem blir skinande rent. Välj mellan veckovis, varannan vecka eller månadsvis städning.",
        "icon": "fa-home",
        "features": ["Dammsugning & moppning", "Badrum & kök", "Dammtorkning", "Fönsterputsning ingår ej"],
        "benefits": ["Flexibla tider", "Miljövänliga medel", "Erfaren personal", "Nöjdhetsgaranti"],
        "order": 1,
    },
    {
        "title": "Flyttstädning",
        "category": "private",
        "subtitle": "Grundlig städning vid flytt",
        "short_description": "Professionell flyttstädning som uppfyller hyresvärdens krav och ger tillbaka din deposition.",
        "description": "Vår flyttstädning är noggrann och grundlig. Vi städar alla ytor, inklusive insidan av skåp, ugn, kylskåp, ugn och fönster. Vi erbjuder garanti på arbetet och återkommer om hyresvärden har anmärkningar.",
        "icon": "fa-truck",
        "features": ["Alla ytor & skåp invändigt", "Ugn & vitvaror", "Fönsterputs", "Garanti ingår"],
        "benefits": ["Garanti på arbetet", "Uppfyller hyresvärdens krav", "Återbesök vid anmärkning", "Snabb bokning"],
        "order": 2,
    },
    {
        "title": "Storstädning",
        "category": "private",
        "subtitle": "Djupstädning av hela hemmet",
        "short_description": "En grundlig storstädning som tar hand om alla de svårare ställena som inte hinns med i vardagen.",
        "description": "Storstädning är en djupgående rengöring av hela hemmet. Vi tar hand om alla de ställen som inte hinns med i vardagen – bakom möbler, inuti skåp, fönsterkarmar, element och mycket mer. Perfekt inför högtider eller när det behövs ett rejält lyft.",
        "icon": "fa-broom",
        "features": ["Bakom & under möbler", "Inuti alla skåp", "Element & fönsterkarmar", "Fönsterputs"],
        "benefits": ["Djupgående rengöring", "Erfaren personal", "Egna rengöringsmedel", "Flexibel bokning"],
        "order": 3,
    },
    {
        "title": "Visningsstädning",
        "category": "private",
        "subtitle": "Städning inför husvisning",
        "short_description": "Gör ditt hem representativt och säljande inför visningen med vår professionella visningsstädning.",
        "description": "En ren och fräsh bostad ger ett bättre intryck vid visning och kan öka försäljningspriset. Vi städar ditt hem noggrant inför visningen så att det ser ut som på bild – skinande rent och välskött.",
        "icon": "fa-eye",
        "features": ["Fönsterputs", "Alla ytor skinande", "Kök & badrum", "Snabb leverans"],
        "benefits": ["Ökar chansen till försäljning", "Professionellt resultat", "Kort varsel möjligt", "Erfaren personal"],
        "order": 4,
    },
    {
        "title": "Fönsterputs",
        "category": "private",
        "subtitle": "Professionell fönsterputsning",
        "short_description": "Klara och skinande fönster som släpper in mer ljus och ger ett fräscht intryck.",
        "description": "Vi putsar dina fönster invändigt och utvändigt med professionell utrustning. Resultatet blir klara, rändelsfria fönster som släpper in maximalt med ljus. Vi hanterar alla typer av fönster inklusive höga och svåråtkomliga.",
        "icon": "fa-window-maximize",
        "features": ["Invändig & utvändig puts", "Fönsterkarmar & spröjsar", "Alla fönstertyper", "Rändelsfritt resultat"],
        "benefits": ["Mer ljus i hemmet", "Professionell utrustning", "Snabbt & effektivt", "Konkurrenskraftiga priser"],
        "order": 5,
    },
    # Företag tjänster
    {
        "title": "Kontorsstädning",
        "category": "company",
        "subtitle": "Regelbunden städning av kontor",
        "short_description": "En ren och välskött arbetsmiljö ökar trivsel och produktivitet. Vi sköter städningen så att ni kan fokusera på er verksamhet.",
        "description": "Vi erbjuder professionell kontorsstädning anpassad efter er verksamhets behov och tider. Oavsett om det gäller daglig städning, veckovis eller efter behov – vi ser till att kontoret alltid är representativt och välskött.",
        "icon": "fa-briefcase",
        "features": ["Daglig eller veckovis", "Kök & toaletter", "Dammtorkning & golv", "Anpassad schema"],
        "benefits": ["Ökad produktivitet", "Professionellt intryck", "Flexibla avtal", "Certifierad personal"],
        "order": 1,
    },
    {
        "title": "Butiksstädning",
        "category": "company",
        "subtitle": "Städning för butiker & affärslokaler",
        "short_description": "En ren butik ger kunderna ett gott intryck. Vi hjälper er att hålla lokalen skinande ren.",
        "description": "Vi erbjuder professionell städning för butiker och affärslokaler. Med vår tjänst kan ni säkerställa att butiken alltid är ren och inbjudande för era kunder. Vi anpassar städschema efter er öppettider.",
        "icon": "fa-store",
        "features": ["Golv & visningsytor", "Skyltfönster", "Toaletter & personalutrymmen", "Anpassat schema"],
        "benefits": ["Inbjudande miljö", "Nöjda kunder", "Flexibla tider", "Regelbunden service"],
        "order": 2,
    },
    {
        "title": "Byggstädning",
        "category": "company",
        "subtitle": "Slutstädning efter byggnation",
        "short_description": "Professionell byggstädning som tar hand om allt byggdamm och smuts efter renovering eller nybyggnation.",
        "description": "Efter renovering eller byggnation finns ofta stora mängder damm och smuts kvar. Vår byggstädning tar hand om allt – vi städar grundligt så att lokalen eller bostaden är inflyttningsklar. Vi hanterar allt från smådamm till grovsmuts.",
        "icon": "fa-hard-hat",
        "features": ["Byggdamm & grovsmuts", "Fönster & glaspartier", "Golv & väggar", "Slutbesiktning"],
        "benefits": ["Inflyttningsklar lokal", "Snabb och effektiv", "Specialutrustning", "Erfaret team"],
        "order": 3,
    },
    {
        "title": "Trappstädning",
        "category": "company",
        "subtitle": "Städning av trapphus & gemensamma utrymmen",
        "short_description": "Vi håller trapphus och gemensamma utrymmen rena och välskötta för era hyresgäster.",
        "description": "Rena trapphus och gemensamma utrymmen är viktigt för trivseln i ett flerbostadshus eller kontorsfastighet. Vi erbjuder regelbunden städning av trapphus, entréer, tvättstugor och andra gemensamma utrymmen.",
        "icon": "fa-building",
        "features": ["Trapphus & entré", "Tvättstuga", "Källargångar", "Regelbunden service"],
        "benefits": ["Nöjda hyresgäster", "Välskött fastighet", "Flexibla avtal", "Pålitlig personal"],
        "order": 4,
    },
    {
        "title": "Golvvård",
        "category": "company",
        "subtitle": "Professionell golvvård & polering",
        "short_description": "Vi återställer och skyddar era golv med professionell golvvård, polering och behandling.",
        "description": "Professionell golvvård förlänger livslängden på era golv och ger dem ett fräscht utseende. Vi hanterar alla typer av golv – parkettgolv, klinker, vinyl och stenplattor. Tjänsterna inkluderar polering, behandling, boning och grundrengöring.",
        "icon": "fa-grip-horizontal",
        "features": ["Alla golvtyper", "Polering & boning", "Skyddsbehandling", "Grundrengöring"],
        "benefits": ["Längre livslängd", "Fräscht utseende", "Professionell utrustning", "Erfaret team"],
        "order": 5,
    },
]


def seed_services(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    for data in SERVICES:
        slug = slugify(data["title"])
        Service.objects.get_or_create(
            slug=slug,
            defaults={
                "title": data["title"],
                "category": data["category"],
                "subtitle": data.get("subtitle", ""),
                "short_description": data.get("short_description", ""),
                "description": data["description"],
                "icon": data.get("icon", ""),
                "features": data.get("features", []),
                "benefits": data.get("benefits", []),
                "order": data.get("order", 0),
                "active": True,
            },
        )


def remove_services(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    titles = [s["title"] for s in SERVICES]
    Service.objects.filter(title__in=titles).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_alter_pricingpackage_id_alter_service_id"),
    ]

    operations = [
        migrations.RunPython(seed_services, remove_services),
    ]
