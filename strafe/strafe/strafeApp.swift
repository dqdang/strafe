//
//  strafeApp.swift
//  strafe
//
//  Created by Derek Dang on 2/1/23.
//

import SwiftUI

@main
struct strafeApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
