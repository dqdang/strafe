//
//  ContentView.swift
//  strafe
//
//  Created by Derek Dang on 2/1/23.
//

import SwiftUI
import CoreData


struct ContentView: View {
    @State private var text = ""
    @FocusState private var isFocused: Bool

    var body: some View {
        NavigationStack {
            Text("")
            TextEditor(text: $text).focused($isFocused).padding(.horizontal)
            }.onTapGesture {
                self.endEditing()
            }.onAppear {
                isFocused = true
            }
    }
    private func endEditing() {
        UIApplication.shared.endEditing()
    }
}

extension UIApplication {
    func endEditing() {
        sendAction(#selector(UIResponder.resignFirstResponder), to: nil, from: nil, for: nil)
    }
}

extension UIScreen{
    static let screenWidth = UIScreen.main.bounds.size.width
    static let screenHeight = UIScreen.main.bounds.size.height
    static let screenSize = UIScreen.main.bounds.size
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView().environment(\.managedObjectContext, PersistenceController.preview.container.viewContext)
    }
}
